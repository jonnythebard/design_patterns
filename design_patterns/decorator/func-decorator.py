import time


def time_it(func):
    def wrapper():
        print("time_it enabled")
        start = time.time()
        result = func()
        end = time.time()
        print(f'{func.__name__} took {int((end-start)*1000)}ms')
        return result

    return wrapper


@time_it
def some_op():
    # get's called inside time_it
    print('Starting op')
    time.sleep(1)
    print('We are done')
    return 123


if __name__ == '__main__':
    res = some_op()
    print(res)
