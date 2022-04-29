from integration_modules import db_module


class DBModule(db_module.DBModule):

    def __init__(self, host, user, pswd, db, read_host=None):
        super().__init__(host=host, user=user, pswd=pswd, db=db, read_host=read_host)

    def insert_records(self, values, headers, str_values):
        query = f"""insert ignore into platform.trans{headers} values {str_values} """
        print(query)
        exit()
        rows = self.queryForBulkInsert(query, values)
        return rows
