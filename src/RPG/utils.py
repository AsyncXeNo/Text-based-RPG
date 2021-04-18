import string
import random


def code_generator(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))
