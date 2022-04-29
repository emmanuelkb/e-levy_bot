import os


class Configurator(object):

    def __init__(self):
        self.region = "eu-west-1"
        self.set_queue_url()

    def get_region(self):
        return self.region

    def set_queue_url(self):
        self.queue_url = os.environ["queue_url"]

    def get_queue_url(self):
        return self.queue_url
