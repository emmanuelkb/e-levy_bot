import boto3


class SSMOps(object):
    def __init__(self, region_name='eu-west-1'):
        # initialize Variables
        self.client = self.getClient(region_name)

    def getClient(self, region_name):
        try:
            client = boto3.client('ssm', region_name=region_name)
            return client
        except Exception as error:
            print(error)
            print("Failed to initialize client..\nExitting...")
            exit()

    def getParameter(self, parameter):
        try:
            response = self.client.get_parameter(Name=parameter, WithDecryption=True)
            return response['Parameter']['Value']
        except Exception as err:
            print(err)
            return False
