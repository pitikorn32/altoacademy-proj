from threading import Thread, Event
from queue import Queue
import time
import random


class producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)  # generrate item
            self.queue.put(item)  # put into queue
            """
            2 possibilities when call queue.put()
              - if optional args block is true and timeout is None: block until a free slot is available
              - if block is false: put item in queue if a free slot is immediately available or raise the full exception
            """
            print(f"Producer notify: item N°{item} appended to queue by {self.name}\n")
            time.sleep(1)


class consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print(f"Consumer notify : {item} popped from queue by {self.name}")
            self.queue.task_done()


if __name__ == "__main__":
    queue = Queue()
    t1 = producer(queue)
    t2 = consumer(queue)
    t3 = consumer(queue)
    t4 = consumer(queue)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
