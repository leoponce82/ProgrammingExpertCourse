# Write your code here.
from threading import Thread, Lock
from time import sleep

usr_num = int(input("Enter a positive int: "))

lock1 = Lock()
lock2 = Lock()

def foo(num, start_lock, end_lock):
    for i in range(num):
        start_lock.acquire()
        print("foo", end="")
        end_lock.release()


def bar(num, start_lock, end_lock):
    for i in range(num):
        start_lock.acquire()
        print("bar", end="")
        end_lock.release()

lock2.acquire()

foo_thread = Thread(target = foo, args=(usr_num, lock1, lock2))
bar_thread = Thread(target = bar, args=(usr_num, lock2, lock1))

foo_thread.start()
bar_thread.start()

foo_thread.join()
bar_thread.join()
