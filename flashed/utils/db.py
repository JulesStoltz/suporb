import sqlite3


class DB:

    def __init__(self, dbFile):
        self.dbFile = dbFile
        self.connection = None
        self.cursor = None

    def _call(self, script):
        """Calls the given script on the dbFile using the executescript method.
        This method does not return a result table. Calls requiring a result 
        table should use the _callback method."""

        try:
            self._openDB()
            self.cursor.executescript(script)
            self._closeDB()

        except Exception as e:
            print(f'[INTERRUPT] Unable to execute - {script}:\n   ', e)

    def _callback(self, script):
        """Calls the given script on the dbFile using the execute method. This
        method returns a result table as a dictionary. Calls that don't require
        a result table should use the _call method."""

        result = {}

        try:
            self._openDB()
            self.cursor.execute(script)
            result = self.cursor.fetchall()
            self._closeDB()

        except Exception as e:
            print(f'[INTERRUPT] Unable to execute - {script}:\n   ', e)

        return result

    def _openDB(self):
        """Creates a connection to the dbFile and sets the connection and
        cursor attributes."""

        try:
            self.connection = sqlite3.connect(self.dbFile)
            self.cursor = self.connection.cursor()

        except Exception as e:
            print('[INTERRUPT] Unable to connect to the database:\n   ', e)

    def _closeDB(self):
        """Closes an active dbFile connection and sets the connection and cursor
        attributes to None."""

        try:
            self.connection.commit()
            self.connection.close()
            self.connection = None
            self.cursor = None

        except Exception as e:
            print('[INTERRUPT] Unable to close database:\n   ', e)

    def addTable(self, name, *columns, pkCols=[]):
        """Adds a table of given name if one does not exist. Table *columns are 
        string args, such as 'word', for column heading names. Table columns
        are created in the order provided. If pkCols is not provided, primary 
        key will be a default incremented integer. Otherwise, primary key(s) 
        will be assigned from list. """

        # Create execution string
        exSTR = "CREATE TABLE if not exists "
        exSTR += f"{name}("
        numCols = len(columns)
        count = numCols
        numPKcols = len(pkCols)
        for value in columns:
            if count == numCols:        # Format for first col
                exSTR += f"{value}"
            elif count > 0:             # Add all remaining cols
                exSTR += f", {value}"
            count -= 1
        
        if numPKcols > 0:
            exSTR += ', PRIMARY KEY ('    # Add primary keys
            for pkcol in pkCols:
                if numPKcols == len(pkCols):
                    exSTR += f"{pkcol}"
                else:
                    exSTR += f", {pkcol}"
                numPKcols -= 1
            exSTR += '))'
        else:
            exSTR += ")"

        # Execute
        self._call(exSTR)

    def addRow(self, table, **fields):
        """Adds row to given table. Table **fields are kwargs of format:
            columnName=rowValue
            Examples: word='blue', count=0, use='NULL'
        
        If insufficient fields are provided, whether by errors in either
        column names or column count, the method will fail.
        
        It is advised to use getColNames method first to ensure no name or 
        count issues occur."""

        # Create execution string
        exSTR = f"INSERT INTO {table} VALUES ("
        count = len(fields)
        for value in fields.values():
            if count > 1:
                if type(value) == str:
                    exSTR += f"'{value}', "
                else: exSTR += f"{value}, "
            else:
                if type(value) == str:
                    exSTR += f"'{value}')"
                else: exSTR += f"{value})"
            count -= 1

        # Execute
        self._call(exSTR)

    def getColCount(self, table):
        """Returns the number of columns in the given table."""

        exSTR = "PRAGMA table_info(%s)" % table
        colDetails = self._callback(exSTR)
        return len(colDetails)

    def getColNames(self, table):
        """Returns a list of column names for the given table."""

        colNames = []
        exSTR = "PRAGMA table_info(%s)" % table
        colDetails = self._callback(exSTR)
        for info in colDetails:
            colNames.append(info[1])
        return colNames

    def readTable(self, table):
        """Returns a dictionary of all rows in the given table."""

        exSTR = f"SELECT * from {table}"
        return self._callback(exSTR)

    def removeTable(self): # TODO: Implement removeTable
        pass

    def removeRow(self): # TODO: Implement removeRow
        pass

    def updateRow(self): # TODO: Implement updateRow
        pass


if __name__ == '__main__':
    db = DB('test.db')
    #db._openDB()