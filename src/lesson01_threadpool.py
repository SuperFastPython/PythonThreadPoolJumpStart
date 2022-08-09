# SuperFastPython.com
# example running a function in the thread pool
from multiprocessing.pool import ThreadPool

# custom function to be executed in a worker thread
def task():
    # report a message
    print('This is another thread')

# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPool() as pool:
        # issue the task
        async_result = pool.apply_async(task)
        # wait for the task to finish
        async_result.wait()
    # close the thread pool automatically
