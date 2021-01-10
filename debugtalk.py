import time

from httprunner import __version__


def get_httprunner_version():
    return __version__

def get_timestamp():
    return  str(int(time.time()*1000))

def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)
