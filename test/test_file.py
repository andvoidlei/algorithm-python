
import numpy as np

matrix = np.zeros((10, 12))
for line in open("./../data/aaa.txt"):
    print(line)
    print(line.split())
    user, item, _,_ = line.split(',')
    user = int(user)
    item = int(item)
    count = 1.0
    matrix[user-1,item-1] = count
    print(matrix)

class A(object):
    def __method(self):
        print ("I'm a method in A")
    def method(self):
        self.__method()

class B(A):
    def __method(self):
        print ("I'm a method in B")

b = B()
b.method()

#a = A()
#a.method()



