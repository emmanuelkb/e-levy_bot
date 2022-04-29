import os
from integration_modules.parameter_store_module import SSMOps


class Configurator(object):

    def __init__(self):
        self.param_store_agent = SSMOps.SSMOps()
        self.setLoggingConfig()

    def setLoggingConfig(self):
        self.log_conf = {
            "log_group": "test",
            "log_stream": "teststream",
        }

    def getLoggingConfig(self):
        return self.log_conf
