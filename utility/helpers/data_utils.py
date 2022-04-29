import random
import string
from datetime import datetime


def get_random_string():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(6))


def get_headers(data):
    if data:
        _ = [tuple(record.keys()) for record in data]
        headers = ", ".join([rec for rec in list(_[0])])
        return headers


def form_strings(data):
    strings = ",".join(['%s ' for _ in list(data[0])])
    return strings


def batch_records(data):
    max_size = 200
    return [data[x:x + max_size] for x in range(0, len(data), max_size)]
