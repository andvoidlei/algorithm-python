# -*- coding:utf-8*-

import kMeans
from numpy import *
import matplotlib.pyplot as plt


def showCluster(dataSet, k, centroids, clusterAssment):
    m, dim = shape(dataSet)
    if dim != 2:
        print("Sorry! i can not draw because the dimension of data is not 2!")
        return 1

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print("Sorry! Your k is too large!")
        return 1
    # draw all samples
    for i in range(m):
        markIndex = int(clusterAssment[i, 0])  # 为样本指定颜色
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    # draw the centroids
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], marker='+', color='red', markersize=18)
        # 用marker来指定质心样式，用color和markersize来指定颜色和大小

    plt.show()


datMat=mat(kMeans.loadDataSet('../data/kMeans_testSet.txt'))

clusterCenters,clusterAssment = kMeans.kMeans(datMat,4)
showCluster(datMat,4,clusterCenters,clusterAssment)