import random
import string
import pandas


def get_random_string():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(6))


def form_strings(data):
    strings = ",".join(['%s ' for _ in list(data)])
    return f"({strings})"
