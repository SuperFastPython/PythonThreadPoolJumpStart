# SuperFastPython.com
# example initializing worker threads in the pool
from time import sleep
from multiprocessing.pool import ThreadPool

# custom function to be executed in a worker thread
def task():
    # report a message
    print('Worker executing task...')
    # block for a moment
    sleep(1)

# initialize a worker in the thread pool
def initialize_worker():
    # report a message
    print('Initializing worker...')

# protect the entry point
if __name__ == '__main__':
    # create and configure the thread pool
    with ThreadPool(2, initializer=initialize_worker) as pool:
        # issue tasks to the thread pool
        for _ in range(4):
            pool.apply_async(task)
        # close the thread pool
        pool.close()
        # wait for all tasks to complete
        pool.join()
