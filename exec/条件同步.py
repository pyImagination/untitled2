import threading
import time

con = threading.Condition()
class Producer(threading.Thread):
    def __init__(self):
        super(Producer, self).__init__()
    def run(self):
        global x
        while True:

            time.sleep(1)
            print('p', x)
            with con:
                if x>0:
                    print('p', '阻塞')
                    con.wait()
                print('produce')
                for i in range(2):
                    x+=1
                    print('producing ...'+str(x))
                print('p', '唤醒')
                con.notify()
class Consumer(threading.Thread):
    def __init__(self):
        super(Consumer, self).__init__()
    def run(self):
        global x
        while True:
            print('c',x)
            with con:

                if x<1:
                    print('c', '阻塞')
                    con.wait()


                x-=1
                print('consuming...'+str(x))
                time.sleep(3)
                con.notify()

x=0
print('start consumer')
c=Consumer()
print('start producer')
p=Producer()
c.start()
p.start()
c.join()
p.join()
print('main thread over!')