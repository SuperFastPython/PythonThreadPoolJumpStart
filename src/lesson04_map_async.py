# SuperFastPython.com
# example executing multiple tasks asynchronously
from multiprocessing.pool import ThreadPool

# custom function to be executed in a worker thread
def task(arg):
    # report a message
    print(f'From another thread {arg}')
    # return a value
    return arg * 2

# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPool() as pool:
        # issue multiple tasks to the pool
        async_result = pool.map_async(task, range(10))
        # handle return values once all tasks completed
        for result in async_result.get():
            print(result)
