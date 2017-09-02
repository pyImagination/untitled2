from  queue import Queue
import random
import threading
import time


class Producer(threading.Thread):
    def __init__(self,queue):
        super(Producer, self).__init__()
        self.queue=queue
    def run(self):
        for i in range(5):
            print("%s:%s is producing %d to the queue!\n"%(time.time(),self.getName(),i))
            self.queue.put(i)
            time.sleep(random.randrange(10)/5)
        print("%s :%s finished!"%(time.time(),self.getName()))

class Consumer(threading.Thread):
    def __init__(self,queue):
        super(Consumer, self).__init__()
        self.queue=queue
    def run(self):
        for i in range(5):
            print("%s: %s is consuming %d to the queue! \n"%(time.time(),self.getName(),i))
            self.queue.get(i)
            time.sleep(random.randrange(10))
        print("%s:%s finish!"%(time.time(),self.getName()))
if __name__ == '__main__':
    queue=Queue()
    producer=Producer(queue)
    consumer=Consumer(queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print('All threads terminate!')
