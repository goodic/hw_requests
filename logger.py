from functools import wraps
import os
from datetime import datetime


def parametrized_logger(log_path):
    def logger(old_function):

        @wraps(old_function)
        def new_function(*args, **kwargs):
            timestmp = datetime.now()
            result = old_function(*args, **kwargs)
            with open(log_path, 'w') as f:
                f.write(f'{timestmp} {old_function.__name__} with params {args} and {kwargs}. Result: {result}')
            return result
        return new_function
    return logger