from integration_modules.sqs_module import sqs_wrapper
from configurator import sqs_config


def sqs_base():
    sqs_conf = sqs_config.Configurator()
    sqs_url = sqs_conf.get_queue_url()
    sqs_module = sqs_wrapper.SQS(sqs_url['setQ'])
    return sqs_module
