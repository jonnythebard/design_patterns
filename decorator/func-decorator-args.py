from functools import wraps
import time


def time_it_with_msg(msg):
    def inner(func):
        @wraps(func)
        def time_it():
            print("time_it enabled")
            print(msg)
            start = time.time()
            result = func()
            end = time.time()
            print(f'{func.__name__} took {int((end-start)*1000)}ms')
            return result
        return time_it
    return inner


@time_it_with_msg("hello?")
def some_op():
    # get's called inside time_it
    print('Starting op')
    time.sleep(1)
    print('We are done')
    return 123


if __name__ == '__main__':
    res = some_op()
    print(res)
