from reversing import *

def task(a):
    pass
A = []
pool = ThreadPool(12)
pool.add_task(task,A)
pool.wait_completion()