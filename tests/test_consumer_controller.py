import json
import unittest
from configurator import database
from models import platform_model


class TestController(unittest.TestCase):
    # db_mod = order_model.DBModule(host="54.155.180.71", user="emmanuel", pswd="Emmanuel1234!@#$&", db="fd")

    db_config_module = database.Configurator()
    DB_CREDENTIALS = db_config_module.getDBCredentials()
    db_mod = platform_model.DBModule(
        host=DB_CREDENTIALS["db_host"],
        user=DB_CREDENTIALS["db_user"],
        pswd=DB_CREDENTIALS["db_pswd"],
        db=DB_CREDENTIALS["db"],
        read_host=DB_CREDENTIALS["db_read_host"]
    )

    def test_successful_insert(self):
        pass
