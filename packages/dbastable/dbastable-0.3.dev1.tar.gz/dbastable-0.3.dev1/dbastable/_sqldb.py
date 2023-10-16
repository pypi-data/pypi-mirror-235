import sqlite3 as sql
import numpy as np
import logging

from ._viewers import (
    SQLTable,
    SQLRow,
    SQLColumn
)
from ._sanitizer import _SanitizerMixin
from .where import _WhereParserMixin, Where
from ._def import _ID_KEY, _B32_COL_PREFIX
from ._broadcaster import broadcast


__all__ = ['SQLDatabase', 'SQLTable', 'SQLRow', 'SQLColumn']


class _RowAccessorMixin:
    """Access and manipulate rows."""
    def _add_missing_columns(self, table, columns):
        """Add missing columns to the table."""
        existing = set(self.column_names(table,
                                         do_not_decode=True))

        for col in [i for i in columns
                    if self._sanitize_colnames(i) not in existing]:
            self.add_column(table, col)

    @staticmethod
    def _fix_row_index(row, length):
        """Fix the row number to be a valid index."""
        if row < 0:
            row += length
        if row >= length or row < 0:
            raise IndexError('Row index out of range.')
        return row

    @staticmethod
    def _dict2row(cols, row):
        values = [None]*len(cols)
        for i, c in enumerate(cols):
            if c in row.keys():
                values[i] = row[c]
            else:
                values[i] = None
        return values

    def _add_data_dict(self, table, data, add_columns=False,
                       skip_sanitize=False):
        """Add data sotred in a dict to the table."""
        data = self._sanitize_colnames(data)
        if add_columns:
            self._add_missing_columns(table, data.keys())

        row_list = self._dict2row(cols=self.column_names(table,
                                                         do_not_decode=True),
                                  row=data)
        try:
            rows = np.broadcast(*row_list)
        except ValueError:
            rows = broadcast(*row_list)
        rows = list(zip(*rows.iters))
        self._add_data_list(table, rows, skip_sanitize=skip_sanitize)

    def _add_data_list(self, table, data, skip_sanitize=False):
        """Add data stored in a list to the table."""
        if np.ndim(data) not in (1, 2):
            raise ValueError('data must be a 1D or 2D array.')

        if np.ndim(data) == 1:
            data = np.reshape(data, (1, len(data)))

        if np.shape(data)[1] != len(self.column_names(table)):
            raise ValueError('data must have the same number of columns as '
                             'the table.')

        if not skip_sanitize:
            data = [tuple(map(self._sanitize_value, d)) for d in data]
        comm = f"INSERT INTO {table} VALUES "
        comm += f"(NULL, {', '.join(['?']*len(data[0]))})"
        comm += ';'
        self.executemany(comm, data)

    def add_rows(self, table, data, add_columns=False, skip_sanitize=False):
        """Add a dict row to a table.

        Parameters
        ----------
        data : dict, list or `~numpy.ndarray`
            Data to add to the table. If dict, keys are column names,
            if list, the order of the values is the same as the order of
            the column names. If `~numpy.ndarray`, dtype names are interpreted
            as column names.
        add_columns : bool (optional)
            If True, add missing columns to the table.
        """
        self._check_table(table)
        if isinstance(data, (list, tuple)):
            return self._add_data_list(table, data,
                                       skip_sanitize=skip_sanitize)
        if isinstance(data, dict):
            return self._add_data_dict(table, data, add_columns=add_columns,
                                       skip_sanitize=skip_sanitize)
        if isinstance(data, np.ndarray):
            names = data.dtype.names
            if names is not None:
                data = {n: data[n] for n in names}
                return self._add_data_dict(table, data,
                                           add_columns=add_columns,
                                           skip_sanitize=skip_sanitize)
            return self._add_data_list(table, data,
                                       skip_sanitize=skip_sanitize)

        # support astropy tables without import it
        if data.__class__.__name__ == 'Table' and \
           data.__class__.__module__ == 'astropy.table.table':
            data = {c: list(data[c]) for c in data.colnames}
            return self._add_data_dict(table, data, add_columns=add_columns,
                                       skip_sanitize=skip_sanitize)

        raise TypeError('data must be a dict, list, or numpy array. '
                        f'Not {type(data)}.')

    def delete_row(self, table, index):
        """Delete a row from the table."""
        self._check_table(table)
        row = self._fix_row_index(index, len(self[table]))
        comm = f"DELETE FROM {table} WHERE {_ID_KEY}={row+1};"
        self.execute(comm)
        self._update_indexes(table)

    def get_row(self, table, index):
        """Get a row from the table."""
        self._check_table(table)
        index = self._fix_row_index(index, len(self[table]))
        return SQLRow(self, table, index)

    def set_row(self, table, row, data):
        """Set a row in the table."""
        row = self._fix_row_index(row, self.count(table))
        colnames = self.column_names(table)

        if isinstance(data, dict):
            data = self._dict2row(colnames, **data)
        elif isinstance(data, (list, tuple, np.ndarray)):
            if len(data) != len(colnames):
                raise ValueError('data must have the same length as the '
                                 'table.')
        else:
            raise TypeError('data must be a dict, list, or numpy array. '
                            f'Not {type(data)}.')

        comm = f"UPDATE {table} SET "
        comm += f"{', '.join(f'{i}=?' for i in colnames)} "
        comm += f" WHERE {_ID_KEY}=?;"
        self.execute(comm,
                     tuple(list(map(self._sanitize_value, data)) + [row+1]))


class _ColumnAccessorMixin:
    """Access and manipulate columns."""

    def add_column(self, table, column, data=None):
        """Add a column to a table."""
        self._check_table(table)

        # check if the original column name is already in the table
        if column.lower() in self.column_names(table):
            raise ValueError(f'Column "{column}" already exists.')

        if data is not None and len(data) != len(self[table]) and \
           len(self[table]) != 0:
            raise ValueError("data must have the same length as the table.")

        # get the real column name (encoded if needed)
        col = self._sanitize_colnames([column])[0]
        comm = f"ALTER TABLE {table} ADD COLUMN '{col}' ;"
        self.logger.debug('adding column "%s" to table "%s"', col, table)
        self.execute(comm)

        # adding the data to the table
        if data is not None:
            self.set_column(table, column, data)

    def delete_column(self, table, column):
        """Delete a column from a table."""
        self._check_table(table)

        if column in (_ID_KEY, 'table', 'default'):
            raise ValueError(f"{column} is a protected name.")
        if column not in self.column_names(table):
            raise KeyError(f'Column "{column}" does not exist.')

        comm = f"ALTER TABLE {table} DROP COLUMN '{column}' ;"
        self.logger.debug('deleting column "%s" from table "%s"',
                          column, table)
        self.execute(comm)

    def set_column(self, table, column, data):
        """Set a column in the table."""
        tablen = self.count(table)
        column = column.lower()

        if column.lower() not in self.column_names(table):
            raise KeyError(f"column {column} does not exist.")

        if len(data) != tablen and tablen != 0:
            raise ValueError("data must have the same length as the table.")

        if tablen == 0:
            for i in range(len(data)):
                self.add_rows(table, {})

        col = self._get_column_name(table, column)
        comm = f"UPDATE {table} SET "
        comm += f"{col}=? "
        comm += f" WHERE {_ID_KEY}=?;"
        args = list(zip([self._sanitize_value(d) for d in data],
                        range(1, self.count(table)+1)))
        self.executemany(comm, args)

    def get_column(self, table, column):
        """Get a column from the table."""
        column = column.lower()
        if column not in self.column_names(table):
            raise KeyError(f"column {column} does not exist.")
        return SQLColumn(self, table, column)


class _TableAccessorMixin:
    """Access and manipulate tables."""

    def _check_table(self, table):
        """Check if the table exists in the database."""
        if table not in self.table_names:
            raise KeyError(f'Table "{table}" does not exist.')

    def add_table(self, table, columns=None, data=None):
        """Create a table in database."""
        self.logger.debug('Initializing "%s" table.', table)
        if table in self.table_names:
            raise ValueError('table {table} already exists.')

        comm = f"CREATE TABLE '{table}'"
        comm += f" (\n{_ID_KEY} INTEGER PRIMARY KEY AUTOINCREMENT"

        if columns is not None and data is not None:
            raise ValueError('cannot specify both columns and data.')
        if columns is not None:
            comm += ",\n"
            for i, name in enumerate(columns):
                comm += f"\t'{name}'"
                if i != len(columns) - 1:
                    comm += ",\n"
        comm += "\n);"

        self.execute(comm)

        if data is not None:
            self.add_rows(table, data, add_columns=True)

    def drop_table(self, table):
        """Drop a table from the database."""
        self._check_table(table)
        comm = f"DROP TABLE {table};"
        self.execute(comm)

    def get_table(self, table):
        """Get a table from the database."""
        self._check_table(table)
        return SQLTable(self, table)


class _ItemAccessorMixin:
    """Access and manipulate items."""

    def get_item(self, table, column, row):
        """Get an item from the table."""
        self._check_table(table)
        row = self._fix_row_index(row, len(self[table]))
        return self.get_column(table, column)[row]

    def set_item(self, table, column, row, value):
        """Set a value in a cell."""
        row = self._fix_row_index(row, self.count(table))
        col = self._get_column_name(table, column)
        value = self._sanitize_value(value)
        self.execute(f"UPDATE {table} SET {col}=? "
                     f"WHERE {_ID_KEY}=?;", (value, row+1))


class SQLDatabase(_WhereParserMixin, _SanitizerMixin,
                  _ItemAccessorMixin, _RowAccessorMixin,
                  _ColumnAccessorMixin, _TableAccessorMixin):
    """Database creation and manipulation with SQL.

    Parameters
    ----------
    db : str
        The name of the database file. If ':memory:' or None is given, the
        database will be created in memory.
    autocommit : bool (optional)
        Whether to commit changes to the database after each operation.
        Defaults to True.
    logger : `~logging.Logger` (optional)
        Logger to use. If None, a logger will be created.
    allow_b32_colnames : bool (optional)
        With a column name is invalid, it will be encoded in base32 and a
        prefix will be added. This is useful to avoid invalid characters like
        '-' in column names. If False, an error will be raised instead.
    **kwargs
        Keyword arguments to pass to the `~sqlite3.connect` function.

    Notes
    -----
    - '__id__' is only for internal indexing. It is ignored on returns.
    - '__b32__' will be used as prefix for base32 encoded column names. So
      it is not allowed to use this prefix in column names.
    """

    def __init__(self, db=None, autocommit=True, logger=None,
                 allow_b32_colnames=False, **kwargs):
        self._db = db
        self._con = sql.connect(self._db or ':memory:', **kwargs)
        self._cur = self._con.cursor()
        self.autocommit = autocommit
        self.logger = logger or logging.getLogger(__name__)
        self._allow_b32_colnames = allow_b32_colnames
        # self._con.set_trace_callback(self.logger.debug)
        # self._con.set_trace_callback(print)

    def execute(self, command, arguments=None):
        """Execute a SQL command in the database."""
        self.logger.debug('executing sql command: "%s"',
                          str.replace(command, '\n', ' '))
        try:
            if arguments is None:
                self._cur.execute(command)
            else:
                self._cur.execute(command, arguments)
            res = self._cur.fetchall()
        except sql.Error as e:
            self._con.rollback()
            raise e

        if self.autocommit:
            self.commit()
        return res

    def executemany(self, command, arguments):
        """Execute a SQL command in the database."""
        self.logger.debug('executing sql command: "%s"',
                          str.replace(command, '\n', ' '))

        try:
            self._cur.executemany(command, arguments)
            res = self._cur.fetchall()
        except sql.Error as e:
            self._con.rollback()
            raise e

        if self.autocommit:
            self.commit()
        return res

    def commit(self):
        """Commit the current transaction."""
        self._con.commit()

    def count(self, table, where=None):
        """Get the number of rows in the table."""
        self._check_table(table)
        comm = "SELECT COUNT(*) FROM "
        comm += f"{table} "
        where, args = self._parse_where(table, where)
        if where is not None:
            comm += f"WHERE {where}"
        comm += ";"
        return self.execute(comm, args)[0][0]

    def select(self, table, columns=None, where=None, order=None, limit=None,
               offset=None):
        """Select rows from a table.

        Parameters
        ----------
        columns : list (optional)
            List of columns to select. If None, select all columns.
        where : dict (optional)
            Dictionary of conditions to select rows. Keys are column names,
            values are values to compare. All rows equal to the values will
            be selected. If None, all rows are selected.
        order : str (optional)
            Column name to order by.
        limit : int (optional)
            Number of rows to select.
        """
        self._check_table(table)
        if columns is None:
            columns = self[table].column_names
        columns = np.atleast_1d(columns)
        # only use sanitized column names
        columns = ', '.join([self._get_column_name(table, c) for c in columns])

        comm = f"SELECT {columns} "
        comm += f"FROM {table} "
        args = []

        where, args_w = self._parse_where(table, where)
        if where is not None:
            comm += f"WHERE {where} "
            # values need to be sanitized
            args += args_w

        if order is not None:
            order = np.atleast_1d(order)
            # only operates on real column names
            order = [self._get_column_name(table, o) for o in order]
            comm += f"ORDER BY {', '.join(order)} ASC "

        if limit is not None:
            comm += "LIMIT ? "
            if not isinstance(limit, (int, np.integer)):
                raise TypeError('limit must be an integer.')
            # force integer
            args.append(int(limit))
        if offset is not None:
            if limit is None:
                raise ValueError('offset cannot be used without limit.')
            if not isinstance(offset, (int, np.integer)):
                raise TypeError('offset must be an integer.')
            comm += "OFFSET ? "
            # force integer
            args.append(int(offset))

        comm = comm + ';'

        if args == []:
            args = None
        res = self.execute(comm, args)
        return res

    def copy(self, indexes=None):
        """Get a copy of the database."""
        return self.__copy__(indexes=indexes)

    def column_names(self, table, do_not_decode=False):
        """Get the column names of the table."""
        self._check_table(table)

        # we get the column names from the cursor descriptor, so we need to
        # select a line
        comm = "SELECT * FROM "
        comm += f"{table} LIMIT 1;"
        self.execute(comm)

        # put the names in this list. Useful to handle encoded names
        columns = []
        for i in self._cur.description:
            if i[0].lower() == _ID_KEY.lower():
                # skip id key. This should not be included in the list
                continue
            # handle encoded names
            if i[0].startswith(_B32_COL_PREFIX) and \
               self._allow_b32_colnames:
                if not do_not_decode:
                    columns.append(self._decode_b32(i[0]))
                else:
                    columns.append(i[0])  # do not lower the names here
            else:
                # always return a lowered normal name
                columns.append(i[0].lower())
        return columns

    @property
    def db(self):
        """Get the database name."""
        return str(self._db)

    @property
    def table_names(self):
        """Get the table names in the database."""
        comm = "SELECT name FROM sqlite_master WHERE type='table';"
        return [i[0] for i in self.execute(comm) if i[0] != 'sqlite_sequence']

    def _get_indexes(self, table):
        """Get the indexes of the table."""
        comm = f"SELECT {_ID_KEY} FROM {table};"
        return [i[0] for i in self.execute(comm)]

    def _update_indexes(self, table):
        """Update the indexes of the table."""
        rows = list(range(1, self.count(table) + 1))
        origin = self._get_indexes(table)
        comm = f"UPDATE {table} SET {_ID_KEY} = ? WHERE {_ID_KEY} = ?;"
        self.executemany(comm, zip(rows, origin))

    def index_of(self, table, where):
        """Get the index(es) where a given condition is satisfied."""
        indx = self.select(table, _ID_KEY, where=where)
        if len(indx) == 1:
            return indx[0][0]-1
        return [i[0]-1 for i in indx]

    def __len__(self):
        """Get the number of rows in the current table."""
        return len(self.table_names)

    def __del__(self):
        """Delete the class, closing the db connection."""
        # ensure connection is closed.
        self._con.close()

    def __setitem__(self, item, value):
        """Set a row in the table."""
        if not isinstance(item, tuple):
            raise KeyError('item must be a in the formats '
                           'db[table, row], db[table, column] or '
                           'db[table, column, row].')
        if not isinstance(item[0], str):
            raise KeyError('first item must be the table name.')
        self.get_table(item[0])[item[1:]] = value

    def __getitem__(self, item):
        """Get a items from the table."""
        if isinstance(item, (str, np.str_)):
            return self.get_table(item)
        if isinstance(item, tuple):
            if not isinstance(item[0], str):
                raise ValueError('first item must be the table name.')
            return self.get_table(item[0])[item[1:]]
        raise ValueError('items must be a string for table names, '
                         'or a tuple in the formats. '
                         'db[table, row], db[table, column] or '
                         'db[table, column, row].')

    def __repr__(self):
        """Get a string representation of the table."""
        s = f"{self.__class__.__name__} '{self.db}' at {hex(id(self))}:"
        if len(self) == 0:
            s += '\n\tEmpty database.'
        for i in self.table_names:
            s += f"\n\t{i}: {len(self.column_names(i))} columns"
            s += f" {len(self[i])} rows"
        return s

    def __copy__(self, indexes=None):
        """Copy the database.

        Parameters
        ----------
        indexes : dict, optional
            A dictionary of table names and their indexes to copy.

        Returns
        -------
        db : SQLDatabase
            A copy of the database.
        """
        def _get_data(table, indx=None):
            if indx is None:
                return self.select(table)
            if len(indx) == 0:
                return None
            # indexes must be fixed
            t = self.count(table)
            indx = [self._fix_row_index(i, t) + 1 for i in np.atleast_1d(indx)]
            where = Where(_ID_KEY, 'IN', indx)

            # select will return in sorted way. We need to unsort it
            s = np.argsort(indx).argsort()
            values = self.select(table, where=where)
            return [values[i] for i in s]

        # when copying, always copy to memory
        db = SQLDatabase(':memory:')
        if indexes is None:
            indexes = {}
        for i in self.table_names:
            db.add_table(i, columns=self.column_names(i))
            rows = _get_data(i, indexes.get(i, None))
            if rows is not None:
                db.add_rows(i, rows, skip_sanitize=True)
        return db
