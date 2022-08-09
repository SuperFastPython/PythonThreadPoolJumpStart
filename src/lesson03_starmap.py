# SuperFastPython.com
# example of multiple tasks with multiple arguments
from multiprocessing.pool import ThreadPool

# custom function to be executed in a worker thread
def task(arg1, arg2, arg3):
    # report a message
    print(f'From another thread {arg1}, {arg2}, {arg3}')
    # return a value
    return arg1 + arg2 + arg3

# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPool() as pool:
        # prepare task arguments
        args = [(i, i*2, i*3) for i in range(10)]
        # issue multiple tasks and handle return values
        for result in pool.starmap(task, args):
            print(result)
