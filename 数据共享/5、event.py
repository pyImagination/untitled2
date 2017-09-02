import threading,logging,time
class MyThread9(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
  def run(self):
    global event
    while True:
      if event.isSet():
        logging.warning(self.getName() + " is Running")
        time.sleep(2)
      else:
        logging.warning(self.getName() + " stopped")
        break
event = threading.Event()
event.set()
def Test9():
  t1=[]
  for i in range(6):
    t1.append(MyThread9())
  for i in t1:
    i.start()
  time.sleep(10)
  q =input("Please input exit:")
  if q=="q":
    event.clear()
if __name__=='__main__':
  Test9()