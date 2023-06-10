import multiprocessing
import random
import time


class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 1000)
            self.queue.put(item)
            print(f"Process {self.name} add {item} to a queue")
            time.sleep(1)


class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("Queue is empty.")
                break
            else:
                item = self.queue.get()
                print(f"Process {self.name} got {item} from the queue")
            time.sleep(0.5)


if __name__ == "__main__":
    q = multiprocessing.Queue()

    p = producer(q)
    c = consumer(q)

    p.start()
    c.start()

    p.join()
    c.join()
