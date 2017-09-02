import threading,time

class Mythreading(threading.Thread):
    def __init__(self):
        super(Mythreading, self).__init__()
    def run(self):
        for i in range(10):
            time.sleep(2)
            print (i)


if __name__ == '__main__':
    print ('start main threading')
    thread=Mythreading()
    # thread.setDaemon(False)
    thread.start()
    thread.join()
    for i in range(11,20):
        print(i)