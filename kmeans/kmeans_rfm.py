# -*- coding:utf-8*-
import sys
#sys.setdefaultencoding('utf-8')
import time

time1=time.time()
import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import scale
from sklearn.cluster import KMeans


#####################读取数据################
#file_name='D:/ml_data/testdata_rfm.csv'
file_name='../data/kmeansdata_rfm.csv'
#file_name='D:/ml_data/kmeans_data02.csv'
#data = pd.read_csv('D:/ml_data/kmeans_data01.csv', sep=',', dtype=str, na_filter=False,header=None)
#data = pd.read_csv(file_name, sep=',', dtype=str, na_filter=False,header=None,index_col=[0])
#首行为字段名
data = pd.read_csv(file_name, sep=',', dtype=str, na_filter=False,header=0)
# print data

##################数据标准化##################
feature=scale(data)
print(feature)
####################设定聚类个数##################
k=10

#调用kmeans类
clf = KMeans(n_clusters=k)
s = clf.fit(feature)
#print (s)

#打印中心点
print (clf.cluster_centers_)

#每个样本所属的簇
print (clf.labels_)

#用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
#print('簇评估')
#print (clf.inertia_)
# 2 2562759.70719795
# 4 1231734.8201674868
# 6 656580.4650842586


#保存模型
joblib.dump(clf , '../data/km.pkl')

#载入保存的模型
clf2 = joblib.load('../data/km.pkl')


print ('进行预测')
print (clf2.predict(feature))

##############写出数据###################
data['label']=clf.labels_
#print (data)
print(data.groupby('label').count())

pd.DataFrame.to_csv(data,'../data/kmeans_result.csv')
print(u'聚类完成')