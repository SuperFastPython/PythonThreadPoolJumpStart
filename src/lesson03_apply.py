# SuperFastPython.com
# example of executing a one-off task and waiting
from multiprocessing.pool import ThreadPool

# custom function to be executed in a worker thread
def task():
    # report a message
    print('This is another thread')

# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPool() as pool:
        # issue a task and wait for it to complete
        pool.apply(task)
