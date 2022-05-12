import json
from models import base
from controller import consumer_controller
from integration_modules.cw_module import cw_base
from datetime import datetime, timezone

db_module = base.db_session()
cw_logger = cw_base.base()


def lambda_handler(event, context=None):
    records = event['Records']
    for record in records:
        data = json.loads(record['body'])
        cw_logger.write_single_log_event(str(len(data)) + " transactions have been fetched from queue at " +
                                         str(datetime.now().replace(tzinfo=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")))
        consumer_controller.insert_transactions_from_queue(db_module, cw_logger, data)
