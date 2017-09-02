#coding:u8
from multiprocessing import Process
import os,time


def run_proc(name):
    time.sleep(3)
    print u'子进程运行中,name=%s,pid=%s'%(name,os.getpid())

if __name__ == '__main__':
    print u'父进程%d'%os.getpid()
    P=Process(target=run_proc,args=('test',))
    P.start()
    # P.join()
    print u'子进程已结束'