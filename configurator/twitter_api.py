import os
from integration_modules.parameter_store_module import SSMOps


class Configurator(object):

    def __init__(self):
        self.param_store_agent = SSMOps.SSMOps()
        self.setTwitterCredentials()

    def setTwitterCredentials(self):
        # self.twitter_config = {
        #     'base_url': os.environ["twitter_base_url"],
        #     'app_key': self.param_store_agent.getParameter(os.environ["consumer_key"]),
        #     'app_secret': self.param_store_agent.getParameter(os.environ["consumer_secret"]),
        #     'oauth_token': self.param_store_agent.getParameter(os.environ["access_token"]),
        #     'oauth_token_secret': self.param_store_agent.getParameter(os.environ["token_secret"])
        # }
        self.twitter_config = {
            'base_url': os.environ["twitter_base_url"],
            'app_key': os.environ["consumer_key"],
            'app_secret': os.environ["consumer_secret"],
            'oauth_token':os.environ["access_token"],
            'oauth_token_secret': os.environ["token_secret"]
        }

    def getTwitterCredentials(self):
        return self.twitter_config
