import json
import requests
from requests_oauthlib import OAuth1


class TwitterApi:

    def __init__(self, **kwargs):
        self.base_url = kwargs["base_url"]
        self.auth = OAuth1(kwargs["app_key"], kwargs["app_secret"], kwargs["oauth_token"], kwargs["oauth_token_secret"])
        if "api_key" in kwargs:
            self.api_key = kwargs["api_key"]
            self.header = {"Content-type": "application/json", "x-api-key": self.api_key}
        else:
            self.header = {"Content-type": "application/json"}

    def get_mentions(self, params):
        path = "users/1525224753434398721/mentions"
        full_path = self.base_url + path
        raw_response = requests.get(full_path, headers=self.header, auth=self.auth, params=params)
        response = json.loads(raw_response.content.decode("utf-8"))
        return response

    def reply_mention(self, reply):
        path = "tweets"
        full_path = self.base_url + path
        raw_response = requests.post(full_path, headers=self.header, data=json.dumps(reply), auth=self.auth)
        response = json.loads(raw_response.content.decode("utf-8"))
        return response
