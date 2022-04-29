from configurator import database
from models import platform_model

db_config = database.Configurator()
db_credentials = db_config.getDBCredentials()


def db_session():
    db_module = platform_model.DBModule(
        host=db_credentials["db_host"],
        user=db_credentials["db_user"],
        pswd=db_credentials["db_pswd"],
        db=db_credentials["db"],
        read_host=db_credentials["db_read_host"]
    )
    return db_module
