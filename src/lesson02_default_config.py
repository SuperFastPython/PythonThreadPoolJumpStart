# SuperFastPython.com
# example reporting the details of a default pool
from multiprocessing.pool import ThreadPool

# protect the entry point
if __name__ == '__main__':
    # create a thread pool
    pool = ThreadPool()
    # report the status of the thread pool
    print(pool)
    # close the thread pool
    pool.close()
