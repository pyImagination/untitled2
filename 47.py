import threading,time


def run():
    time.sleep(5)
    for i in range(10):
        print i

for i in range(4):
    a=threading.Thread(target=run,args=())
    a.start()
    # a.join()
for i in range(50,60):
    print i