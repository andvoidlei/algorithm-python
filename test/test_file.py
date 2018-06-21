
import numpy as np

matrix = np.zeros((1, 1))
for line in open("D:/aaa.txt"):
    print(line)
    print(line.split())
    user, item, _ = line.split(',')
    user = int(user)
    item = int(item)
    count = 1.0
    print(user,item)
    count = 1.0
    matrix[user-1,item-1] = count