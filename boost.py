import threading
import time


def boost(callback, _time):
    thread_list = []
    for i in range(len(_time)):
        th = threading.Thread(target = callback, args = (_time[i], i))
        thread_list.append(th)
        th.start()
    for thrd in thread_list:
        thrd.join()
