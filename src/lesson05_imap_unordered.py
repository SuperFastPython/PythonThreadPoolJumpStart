# SuperFastPython.com
# example getting many task results in completion order
from time import sleep
from random import random
from multiprocessing.pool import ThreadPool

# custom function to be executed in a worker thread
def task(arg):
    # block for a random fraction of a second
    sleep(random())
    # report a message
    print(f'From another thread {arg}')
    # return a value
    return arg * 2

# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPool(4) as pool:
        # issue multiple tasks and handle return values
        for rs in pool.imap_unordered(task, range(10)):
            print(rs)
