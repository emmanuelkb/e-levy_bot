import pymysql
from . import DBExceptions


class DBModule():

    def __init__(self, **kwargs):
        try:
            self.host = kwargs["host"]
            self.user = kwargs["user"]
            self.pswd = kwargs["pswd"]
            self.db = kwargs["db"]
            if "port" in kwargs:
                self.port = kwargs["port"]
            else:
                self.port = False
            if "read_host" in kwargs:
                self.read_host = kwargs["read_host"]
            else:
                self.read_host = self.host
            # self.createConnection(self.host, self.user, self.pswd, self.db, self.port)
        except KeyError as error:
            if str(error) == "db":
                raise DBExceptions.DatabaseCredentialException(
                    key_=str(error),
                    msg="db is required, this is an application"
                )
            else:
                raise DBExceptions.DatabaseCredentialException(key_=str(error))

    def createConnection(self, host, user, pswd, db, port=False):
        try:
            if port:
                self.connection = pymysql.connect(host=host, user=user, password=pswd, db=db, port=port)
            self.connection = pymysql.connect(host=host, user=user, password=pswd, db=db)
        except Exception as err:
            raise DBExceptions.DatabaseConnectionException(err)

    def openCursor(self, count=0):
        try:
            self.cursor = self.connection.cursor()
        except BrokenPipeError:
            if count > 3:
                raise ResourceWarning("Connection is Not Recoverable")
            self.createConnection(self.host, self.user, self.pswd, self.db, self.port)
            self.openCursor(count + 1)

    def closeCursor(self):
        self.cursor.close()

    def closeConnection(self):
        self.connection.close()

    def readRecords(self, query, data=None, immediate=False):
        # validate the query once the method become available
        try:
            if immediate:
                self.createConnection(self.host, self.user, self.pswd, self.db, self.port)
            else:
                self.createConnection(self.read_host, self.user, self.pswd, self.db, self.port)
            self.openCursor()
            if data:
                rows = self.cursor.execute(query, data)
            else:
                rows = self.cursor.execute(query)
            if rows < 1:
                raise DBExceptions.RecordNotFoundException()
            results = self.cursor.fetchall()
            self.closeCursor()
            self.closeConnection()
            tray = []
            for result in results:
                hold = [item for item in result]
                tray.append(hold)
            return tray
        except pymysql.err.ProgrammingError as error:
            self.closeCursor()
            self.closeConnection()
            raise DBExceptions.FaultyQueryException()

    def readSingleRecord(self, query, immediate=False):
        return self.readRecords(query, immediate)[0]

    def dataRetrievalQuery(self, query, values=None, immediate=None):
        try:
            if immediate:
                self.createConnection(self.host, self.user, self.pswd, self.db, self.port)
            else:
                self.createConnection(self.read_host, self.user, self.pswd, self.db, self.port)
            tray = []
            self.openCursor()
            if values:
                row_count = self.cursor.execute(query, values)
                field_names = [field[0] for field in self.cursor.description]
                for row in self.cursor:
                    tray.append(dict(zip(field_names, row)))
                self.closeCursor()
                self.closeConnection()
                return tray, row_count
            else:
                row_count = self.cursor.execute(query)
                field_names = [field[0] for field in self.cursor.description]
                for row in self.cursor:
                    tray.append(dict(zip(field_names, row)))
                self.closeCursor()
                self.closeConnection()
                return tray, row_count
        except pymysql.err.ProgrammingError as error:
            self.closeCursor()
            self.closeConnection()
            raise DBExceptions.FaultyQueryException()

    def dataAlterationQuery(self, query, data=None):
        try:
            self.createConnection(self.host, self.user, self.pswd, self.db, self.port)
            self.openCursor()
            if data:
                rows = self.cursor.execute(query, data)
            else:
                rows = self.cursor.execute(query)
            self.connection.commit()
            self.closeCursor()
            self.closeConnection()
            return rows
        except pymysql.err.ProgrammingError as error:
            self.closeCursor()
            self.closeConnection()
            raise DBExceptions.FaultyQueryException()
        except pymysql.err.IntegrityError as error:
            self.closeCursor()
            self.closeConnection()
            raise DBExceptions.IntegrityError(str(error))

    def queryForBulkInsert(self, query, data):
        try:
            self.createConnection(self.host, self.user, self.pswd, self.db, self.port)
            self.openCursor()
            rows = self.cursor.executemany(query, data)
            self.connection.commit()
            self.closeCursor()
            self.closeConnection()
            return rows
        except pymysql.err.ProgrammingError as error:
            self.closeCursor()
            self.closeConnection()
            raise DBExceptions.FaultyQueryException()
        except pymysql.err.IntegrityError as error:
            self.closeCursor()
            self.closeConnection()
            raise DBExceptions.IntegrityError(str(error))
        except TypeError as error:
            print(error)
            print(data)
            return False


    def createRecord(self, query):
        # validate query once method become available
        rows = self.dataAlterationQuery(query)
        if rows < 1:
            raise DBExceptions.RecordNotInsertException()

    def createRecordBulk(self, query, values):
        rows = self.queryForBulkInsert(query, values)
        return rows

    def updateRecord(self, query):
        rows = self.dataAlterationQuery(query)
        if rows < 1:
            raise DBExceptions.RecordToBeUpdateNotFoundException()

    def deleteRecord(self, query, data):
        rows = self.dataAlterationQuery(query, data)
        if rows < 1:
            raise DBExceptions.RecordToBeDeleteNotFoundException()
