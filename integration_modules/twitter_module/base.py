from configurator import twitter_api
from integration_modules.twitter_module import twitter


def base_config():
    config_obj = twitter_api.Configurator()
    credentials = config_obj.getTwitterCredentials()
    config = twitter.TwitterApi(base_url=credentials['base_url'], app_key=credentials['app_key'],
                                app_secret=credentials['app_secret'], oauth_token_secret=credentials['oauth_token_secret'],
                                oauth_token=credentials['oauth_token'])
    return config
