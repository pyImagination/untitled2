#coding:u8
import  multiprocessing

#Array Value共享数据，必须当作参数，
def  f(n,a):
    n.value=9999
    a[0]=8888


if __name__=="__main__":
    arr=multiprocessing.Array("i",[1,2,3,4,5]) #数据共享，当作参数
    num=multiprocessing.Value("d",0.0) #d是一个类型，%d,%s,

    p=multiprocessing.Process(target=f,args=(num,arr))
    p.start()
    p.join()

    print(arr[:])
    print(num.value)



    #mylist=list(range(10))#强转换
    #print(mylist)