import multiprocessing,os
def f(a):


    a.acquire()
    global b
    a.value=a.value+1
    b=b+a.value
    print(b,os.getpid())
    a.release()



b=1
if __name__ == '__main__':
    print('starting')
    list1=[]
    num=multiprocessing.Value('i',1)
    print(num.value)
    print(dir(num))
    for i in range(5):
        p=multiprocessing.Process(target=f,args=(num,))
        list1.append(p)
    for item in list1:
        item.start()
    print(b)
    print('finish!')