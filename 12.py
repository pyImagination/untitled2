def Main():
    print(locals())
    for i in range(3):
        locals()['part'+str(i)] = i
    print(locals())
    print(part0)
a=locals()
Main()
print('4', locals())
print('5',globals())

# print(locals())
# for i in range(3):
#         locals()['part'+str(i)] = i
#         print(locals())
# print(locals())
# print(part0)
