from controller import bot
from integration_modules.twitter_module import base


twitter_module = base.base_config()


def lambda_handler(event, context=None):
    return bot.get_mentions(twitter_module)
