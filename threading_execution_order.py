import threading
from threading import Thread, Lock
from time import sleep
import math


def append_values(lst, values=[], delay=1):
    for value in values:
        lst.append(value)
        print(lst)
        sleep(math.ceil(abs(delay)))


def append_integer(lst, integer):
    lst.append(integer)
    print(lst)


lst = []

# Write your code here.
thread1 = Thread(target=append_values, args=(lst, [1,3,5]))
thread2 = Thread(target=append_integer, args=(lst, 4))
thread3 = Thread(target=append_integer, args=(lst, 3))

thread1.start()
thread2.start()
thread1.join()
thread3.start()

