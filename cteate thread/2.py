import threading
import time

def test_func(id):
    for i in range(5):
        time.sleep(2)
        print('thread %d is running %d'%(id,i))
threadlist=[]
for i in range(10):
    t=threading.Thread(target=test_func,args=(i,))
    threadlist.append(t)
for i in threadlist:
    i.start()

# for i in threadlist:
#     i.join()