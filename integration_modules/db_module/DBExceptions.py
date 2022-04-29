"""
Specific exceptions for DB Module:
    We will update this module for new projects it too old
"""


# Connection
class DatabaseConnectionException(Exception):
    """
    This error is called when db connections fail
    for what ever reason
    """

    def __init__(self, pymysql_msg):
        self.msg = "Failed Connecting to database, please check credentials and, or connectivity"
        self.msg += "\n" + str(pymysql_msg)
        super().__init__(self.msg)

    def __str__(self):
        return self.msg


class DatabaseCredentialException(Exception):
    """
    This error is thrown when the credentials are not 
    added as required
    """

    def __init__(self, key_, msg=""):
        if msg:
            self.msg = msg
        else:
            self.msg = "{} is required".format(key_)
        super().__init__(self.msg)

    def __str__(self):
        return self.msg


# Records
class RecordNotFoundException(Exception):
    def __init__(self):
        self.msg = "Record does not exist"
        super().__init__(self.msg)

    def __str__(self):
        return self.msg


class RecordNotInsertException(Exception):
    def __init__(self):
        self.msg = "Record was not inserted"
        super().__init__(self.msg)

    def __str__(self):
        return self.msg


class RecordToBeUpdateNotFoundException(Exception):
    def __init__(self, msg="Record being updated does not exist"):
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return self.msg


class RecordToBeDeleteNotFoundException(Exception):
    def __init__(self):
        self.msg = "Record being deleted does not exist"
        super().__init__(self.msg)

    def __str__(self):
        return self.msg


# Programming Error
class FaultyQueryException(Exception):
    def __init__(self, err=None):
        self.msg = "There is an error in your query"
        super().__init__(self.msg)

    def __str__(self):
        return self.msg


class IntegrityError(Exception):

    def __init__(self, err_msg="Contraints Failure on table"):
        self.msg = err_msg
        super().__init__(self.msg)

    def __str__(self):
        return self.msg
