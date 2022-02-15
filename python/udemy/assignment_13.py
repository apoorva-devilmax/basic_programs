# import internal packages
from threading import Thread, current_thread


class EvenNumbersThread(Thread):
    def run(self):
        thread_name = current_thread().getName()
        for i in range(2, 11, 2):
            print(f'{thread_name}: {i}')
        # for loop ends here
    # run method ends here
# EvenNumbersThread class ends here


class OddNumbersThread(Thread):
    def run(self):
        thread_name = current_thread().getName()
        for i in range(1, 11, 2):
            print(f'{thread_name}: {i}')
        # for loop ends here
    # run method ends here
# OddNumbersThread class ends here

t1 = EvenNumbersThread()
t2 = OddNumbersThread()
t1.start()
t2.start()
thread_name = current_thread().getName()
for i in range(1, 11):
    print(f'{thread_name}: {i}')
# for loop ends here
