# -*- coding: utf-8 -*-
"""
@create time  2019-10-30 23:40:00

@author: kevin
"""

from numpy import *
from cal_entropy import cal_entropy as cetr
from split_by_entropy import  Split_Data,Split_by_entropy


def create_data():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


if __name__ == '__main__':
    myData, labels = create_data()
    print(myData)
    '''计算熵值'''
    print('熵值：'+str(cetr(myData)))
    print(Split_Data(myData,0,1))  #Split_Data(dataset, axis, value)
    #print(Split_by_entropy(myData))


