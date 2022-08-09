# SuperFastPython.com
# example of configuring a thread pool with many works
from multiprocessing.pool import ThreadPool

# protect the entry point
if __name__ == '__main__':
    # create a thread pool with many workers
    pool = ThreadPool(1000)
    # report the status of the thread pool
    print(pool)
    # close the thread pool
    pool.close()
