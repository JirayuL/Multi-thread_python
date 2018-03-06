import threading
import logging
import random
import time

M= 50
N= 50
def withdraw(acc1, acc2):
   for i in range(M):
     r = random.random()
     logging.debug('Sleeping %0.02f', r)
     time.sleep(r)
     acc1.withdraw(r)
     acc2.withdraw(r)
     print("A:", acc1.value, "B:", acc2.value)
     print("Withdraw: ", r)
     print()
      #print how much you subtract from and new acc value
def deposit(acc1, acc2):
   for i in range(N):
     r = random.random()
     logging.debug('Sleeping %0.02f', r)
     time.sleep(r)
     acc1.withdraw(r)
     acc2.withdraw(r)
     print("A:", acc1.value, "B:", acc2.value)
     print("Deposit:  ", r)
     print()
     # print how much you add and  new acc value

class bankAcc(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start  # initial account value

    def withdraw(self, value):
        logging.debug('Waiting for a lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired a lock')
            self.value = self.value - value
        finally:
            logging.debug('Released a lock')
            self.lock.release()

    def deposit(self, value):
        logging.debug('Waiting for a lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired a lock')
            self.value = self.value + value
        finally:
            logging.debug('Released a lock')
            self.lock.release()

if __name__ == '__main__':
    A = bankAcc(10)
    B = bankAcc(3)

    for i in range(3):
         t = threading.Thread(target=deposit, args=(A,B))
         t.start()
    for i in range(3):
         t = threading.Thread(target=withdraw, args=(A,B))
         t.start()

    main_thread = threading.currentThread()
    for t in threading.enumerate():
         if t is not main_thread:
             t.join()
    logging.debug('A: %d B %d', A.value,B.value)
