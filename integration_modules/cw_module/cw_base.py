from integration_modules.cw_module import cloudwatch
from configurator import cw_logger as logger


def base():
    log = logger.Configurator()
    cw_details = log.getLoggingConfig()
    cw_logger = cloudwatch.CloudWatch(cw_details['log_group'], cw_details['log_stream'])
    return cw_logger
