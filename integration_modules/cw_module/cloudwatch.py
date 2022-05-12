import boto3
import time


class CloudWatch:
    def __init__(self, log_group_name, log_stream, region_name="eu-west-1"):
        """
        :params observability_client: boto3 cloudwatch resource for
        :params log_group_name: cloudwatch log group name resource for
        :params log_stream: boto3 cloudwatch log stream resource for
        """
        self.observability_client = boto3.client('logs', region_name)
        self.cw_sequence_token = None
        self.log_group_name = log_group_name
        self.log_stream = log_stream

    def get_timestamp(self):
        return int(round(time.time() * 10 ** 3))

    def create_log_group(self):
        response = self.observability_client.create_log_group(
            logGroupName=self.log_group_name,
        )
        retention_policy_response = self.observability_client.put_retention_policy(
            logGroupName=self.log_group_name,
            retentionInDays=30
        )

        _ = self.create_log_stream()

    def create_log_stream(self):
        logs_stream_response = self.observability_client.create_log_stream(
            logGroupName=self.log_group_name,
            logStreamName=self.log_stream
        )
        return logs_stream_response

    def put_cloudwatch_log_event(self, message):
        message_payload = {
            'timestamp': self.get_timestamp(),
            'message': message
        }
        if self.cw_sequence_token:
            create_log_response = self.observability_client.put_log_events(
                logGroupName=self.log_group_name,
                logStreamName=self.log_stream,
                logEvents=[
                    message_payload
                ],
                sequenceToken=self.cw_sequence_token)
            print(create_log_response)
        else:
            create_log_response = self.observability_client.put_log_events(
                logGroupName=self.log_group_name,
                logStreamName=self.log_stream,
                logEvents=[
                    message_payload
                ])
            print(create_log_response)
            self.cw_sequence_token = create_log_response["nextSequenceToken"]

        return {"message": "success"}

    def write_single_log_event(self, message):
        try:
            put_event_response = self.put_cloudwatch_log_event(message)
        except self.observability_client.exceptions.DataAlreadyAcceptedException as err_response:
            self.cw_sequence_token = err_response.response["expectedSequenceToken"]
            self.put_cloudwatch_log_event(message)
        except self.observability_client.exceptions.InvalidSequenceTokenException as err_response:
            self.cw_sequence_token = err_response.response["expectedSequenceToken"]
            self.put_cloudwatch_log_event(message)
        except self.observability_client.exceptions.ResourceNotFoundException as error:
            if "log group" in str(error):
                print("log group error")
                _ = self.create_log_group()
            elif "log stream" in str(error):
                print("log stream error")
                _ = self.create_log_stream()
            put_event_response = self.put_cloudwatch_log_event(message)

        return {"message recorded"}

    def put_bulk_cloudwatch_log_event(self, messages):
        bulk_messages = [{"timestamp": self.get_timestamp(), "message": message} for message in messages]
        if self.cw_sequence_token:
            create_log_response = self.observability_client.put_log_events(
                logGroupName=self.log_group_name,
                logStreamName=self.log_stream,
                logEvents=bulk_messages,
                sequenceToken=self.cw_sequence_token)
        else:
            create_log_response = self.observability_client.put_log_events(
                logGroupName=self.log_group_name,
                logStreamName=self.log_stream,
                logEvents=bulk_messages)
            print(create_log_response)
            self.cw_sequence_token = create_log_response["nextSequenceToken"]
        return {"message": "success"}

    def write_bulk_log_events(self, messages):
        try:
            put_event_response = self.put_bulk_cloudwatch_log_event(messages)
        except self.observability_client.exceptions.DataAlreadyAcceptedException as err_response:
            self.cw_sequence_token = err_response.response["expectedSequenceToken"]
            self.put_bulk_cloudwatch_log_event(messages)
        except self.observability_client.exceptions.InvalidSequenceTokenException as err_response:
            self.cw_sequence_token = err_response.response["expectedSequenceToken"]
            self.put_bulk_cloudwatch_log_event(messages)
        except self.observability_client.exceptions.ResourceNotFoundException as error:
            if "log group" in str(error):
                print("log group error")
                _ = self.create_log_group()
            elif "log stream" in str(error):
                print("log stream error")
                _ = self.create_log_stream()
            put_event_response = self.put_bulk_cloudwatch_log_event(messages)
        return {"message recorded"}
