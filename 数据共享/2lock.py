import _thread
import time
mylock = _thread.allocate_lock()  # Allocate a lock
def add_num(name):
    global num
    while True:
        mylock.acquire()  # Get the lock
        # Do something to the shared resource
        print('Thread %s locked! num=%s' % (name, str(num)))
        if num >= 5:
            print('Thread %s released! num=%s' % (name, str(num)))
            mylock.release()
            _thread.exit_thread()
        num += 1
        print('Thread %s released! num=%s' % (name, str(num)))
        mylock.release()  # Release the lock.
def test():
    _thread.start_new_thread(add_num, ('A',))
    _thread.start_new_thread(add_num, ('B',))

num = 0  # Shared resource
if __name__ == '__main__':
    test()
    time.sleep(5)

while True:
    pass