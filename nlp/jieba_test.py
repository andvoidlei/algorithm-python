#coding:utf-8
import jieba

jieba.load_userdict("../data/dict.txt")
words=jieba.cut("他来到了网易杭研大厦")
print ("/".join(words))
print (type(words))