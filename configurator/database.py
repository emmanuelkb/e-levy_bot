"""
Created on Mar 30, 2020

@author: alloteya
"""
import os
from integration_modules.parameter_store_module import SSMOps


class Configurator(object):

    def __init__(self):
        self.param_store_agent = SSMOps.SSMOps()
        self.setDBCredentials()

    def setDBCredentials(self):
        self.db_conf = {
            # "db_host": self.param_store_agent.getParameter(os.environ["db_host"]),
            # "db_user": self.param_store_agent.getParameter(os.environ["db_user"]),
            # "db_pswd": self.param_store_agent.getParameter(os.environ["db_pswd"]),
            # "db": self.param_store_agent.getParameter(os.environ["db"]),
            # "db_read_host": self.param_store_agent.getParameter(os.environ["db_read_host"])
            "db_host": os.environ["db_host"],
            "db_user":os.environ["db_user"],
            "db_pswd": os.environ["db_pswd"],
            "db": os.environ["db"],
            "db_read_host": os.environ["db_read_host"]
        }

    def getDBCredentials(self):
        return self.db_conf
