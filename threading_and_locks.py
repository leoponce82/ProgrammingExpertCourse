# Welcome to our Python playground!

import random
import time
from threading import Lock, Thread


def loop(thread_name, n, lock):
    lock.acquire()
    for i in range(n):
        # Sleep for up to 20 milliseconds.
        
        time.sleep(random.randint(1, 20) / 1000)
        print(f"Thread {thread_name}: {i}")
    lock.release()
    


# TODO: As an exercise, try to change this code to let
# t1 finish first before t2 starts running. (Hint: A
# mutex lock should do the trick)
lock = Lock()

t1 = Thread(target=loop, args=("t1", 10, lock))
t2 = Thread(target=loop, args=("t2", 10, lock))

t1.start()
t2.start()

t1.join()
t2.join()