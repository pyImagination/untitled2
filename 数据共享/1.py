import threading,time
a=0
def add(id):
    global a
    time.sleep(1)
    for i in range(10000):
        a=a+1
        print('threading %d is running'%id,a)

threadlist=[]
for i in range(10):
    t=threading.Thread(target=add,args=(i,))
    threadlist.append(t)

for i in threadlist:
    i.start()