# -*- coding: utf-8 -*-

u"""Producer-Consumer pattern for multiprocessing system"""

__author__ = "Shybkoi"


from multiprocessing import Process, Condition, Queue


class Producer(Process):
    def __init__(self, queue, mutex, name):
        super().__init__()
        self.queue = queue
        self.mutex = mutex
        self.name = name

    def run(self):
        while True:
            self.mutex.acquire()
            while self.queue.qsize() >= 5:
                self.mutex.wait()
            self.queue.put("element")
            self.mutex.notify()
            self.mutex.release()
            print("process %s put element to queue" % self.name)


class Consumer(Process):
    def __init__(self, queue, mutex, name):
        super().__init__()
        self.queue = queue
        self.mutex = mutex
        self.name = name

    def run(self):
        while True:
            self.mutex.acquire()
            while self.queue.qsize() == 0:
                self.mutex.wait()
            self.queue.get()
            self.mutex.notify()
            self.mutex.release()
            print("process %s get element to queue" % self.name)


def main():
    queue = Queue()
    mutex = Condition()

    p1 = Producer(queue, mutex, "p1")
    p2 = Producer(queue, mutex, "p2")
    p3 = Producer(queue, mutex, "p3")

    c1 = Consumer(queue, mutex, "c1")
    c2 = Consumer(queue, mutex, "c2")

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()


if __name__ == "__main__":
    main()


