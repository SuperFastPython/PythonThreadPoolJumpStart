# SuperFastPython.com
# example check status and handle result of async task
from time import sleep
from random import random
from multiprocessing.pool import ThreadPool

# custom function to be executed in a thread worker
def task():
    # loop a few times to simulate a slow task
    for i in range(10):
        # generate a random value between 0 and 1
        value = random()
        # block for a fraction of a second
        sleep(value)
        # report a message
        print(f'>{i} got {value}')

# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPool() as pool:
        # issue a task asynchronously
        async_result = pool.apply_async(task)
        # wait until the task is complete
        while not async_result.ready():
            # report a message
            print('Main thread waiting...')
            # block for a moment
            async_result.wait(timeout=1)
        # report if the task was successful
        if async_result.successful():
            print('Task was successful.')
