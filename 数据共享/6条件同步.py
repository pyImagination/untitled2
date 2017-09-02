import threading
import time


class Producer(threading.Thread):
    def __init__(self, t_name):

        threading.Thread.__init__(self, name=t_name)

    def run(self):

        global x
        while True:
            time.sleep(1)

            print('p', '加锁')
            con.acquire()#加锁

            time.sleep(1)
            if x > 0:

                print('p', '阻塞')
                con.wait()#阻塞


            else:

                for i in range(5):
                    x = x + 1

                    print("producing..." + str(x))

                print('p', '唤醒')
                con.notify()#唤醒


            print("procer",x)

            print('p', '解锁')
            con.release()#解锁



class Consumer(threading.Thread):
    def __init__(self, t_name):

        threading.Thread.__init__(self, name=t_name)

    def run(self):

        global x
        print("consumer1",x)
        while True:
            time.sleep(2)

            print('c', '加锁')
            con.acquire()#加锁


            if x == 0:

                print('consumer wait1')

                print('c', '阻塞')
                con.wait()#阻塞

            else:
                print("consumer2",x)
                for i in range(5):
                    x = x - 1

                    print("consuming..." + str(x))

                time.sleep(1)
                print('c', '唤醒')
                con.notify()#唤醒


            print(x)

            print('c', '解锁')
            con.release()#解锁



con = threading.Condition()

x = 0

print('start consumer')

c = Consumer('consumer')

print('start producer')

p = Producer('producer')

p.start()
c.start()

p.join()

c.join()#阻塞主线程，防止主线程

print("主线程运行完毕",x)