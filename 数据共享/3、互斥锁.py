import threading
import time
mutex=threading.Lock()
class MyThread(threading.Thread):
    def run(self):
        global num
        if mutex.acquire(1):
            num=num+1
            time.sleep(0.1)
            msg=self.name+'set num to '+str(num)
            print(msg)
            mutex.release()
num=0
def test():
    for i in range(5):
        t=MyThread()
        t.start()
if __name__ == '__main__':
    test()