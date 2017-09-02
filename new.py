class A(object):
    print('A')
class B(A):
    def __init__(self):
        print 'B'
        self.name='B'
class C(B):
    # def __new__(cls, *args, **kwargs):
    #     print 'c(b)'
    #     return B.__new__(A)
    def __init__(self):
        self.name='c'
        # print 'C'
    def run(self):
        print('haha')
class D(C):
    def __new__(cls, *args, **kwargs):
        return  B.__new__(C)
d=D()
# b=B()
# print type(b)
d.run()
print type(d)