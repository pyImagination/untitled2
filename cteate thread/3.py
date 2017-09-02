import threading

class a(threading.Thread):
    def __init__(self,id):
        # threading.Thread.__init__(self)
        # super(a, self).__init__()
        super().__init__()
        self.id=id
    def run(self):
        print('this is %d thread runing'%self.id)
for i in range(10):
    thread=a(i)
    thread.start()