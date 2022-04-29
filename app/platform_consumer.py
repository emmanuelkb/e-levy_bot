import json
from models import base
from controller import consumer_controller

db_module = base.db_session()


def lambda_handler(event, context=None):
    records = event['Records']
    for record in records:
        data = json.loads(record['body'])
        consumer_controller.insert_transactions_from_queue(db_module, data)
