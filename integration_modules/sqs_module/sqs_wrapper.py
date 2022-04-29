import boto3
import json
import sys
import uuid


class SQS:
    """
    Wrapper built on SQS
    """

    def __init__(self, queue_url):
        self.client = self.get_sqs_client("eu-west-1")
        self.queue_url = queue_url

    @staticmethod
    def get_sqs_client(region_name):
        try:
            client = boto3.client('sqs', region_name=region_name)
            return client
        except Exception as error:
            print("Failed to initialize SQS client..\nExitting...")
            print(error)

    def send_message(self, msg):
        try:
            response = self.client.send_message(QueueUrl=self.queue_url, MessageBody=json.dumps(msg, default=str),
                                                MessageGroupId=str(msg['meta_base']['base_id']),
                                                MessageDeduplicationId=str(uuid.uuid4()))
            # print(f"messageId: {response['MessageId']}")
            return True
        except Exception as error:
            print(error)
            return False

    def get_message(self):
        try:
            response = self.client.receive_message(QueueUrl=self.queue_url, MaxNumberOfMessages=10, WaitTimeSeconds=20)
            return response
        except Exception as error:
            print(error)
        return False
