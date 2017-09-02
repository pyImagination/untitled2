import _thread,time
def show(ag):
    print('haha'+ag)

for i in range(10):
    _thread.start_new_thread(show,('haha',))


while True:
    time.sleep(1)