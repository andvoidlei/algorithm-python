import jieba
import jieba.analyse
import jieba.posseg

#s = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
#for x, w in jieba.analyse.extract_tags(s, withWeight=True):
#    print("%s %s" % (x, w))

print("上海迪士尼：")
file_name = "../data/prd_content.txt"
content = open(file_name, encoding='utf-8').read()
for x, w in jieba.analyse.extract_tags(content, withWeight=True,topK=20):
    print("%s %s" % (x, w))

print("")
print("黄山风景区：")
file_name = "../data/prd_content_huangshan.txt"
content = open(file_name, encoding='utf-8').read()
for x, w in jieba.analyse.extract_tags(content, withWeight=True,topK=20):
    print("%s %s" % (x, w))


print("")
print("线路：")
file_name = "../data/prd_content_xianlu.txt"
content = open(file_name, encoding='utf-8').read()
for x, w in jieba.analyse.extract_tags(content, withWeight=True,topK=20):
    print("%s %s" % (x, w))

print("")
print("上海迪士尼：")
file_name = "../data/prd_content.txt"
content = open(file_name, encoding='utf-8').read()
for x, w in jieba.analyse.textrank(content, withWeight=True,topK=20):
    print("%s %s" % (x, w))

print("")
print("黄山风景区：")
file_name = "../data/prd_content_huangshan.txt"
content = open(file_name, encoding='utf-8').read()
for x, w in jieba.analyse.textrank(content, withWeight=True,topK=20):
    print("%s %s" % (x, w))


print("")
print("线路textrank：")
file_name = "../data/prd_content_xianlu.txt"
content = open(file_name, encoding='utf-8').read()
for x, w in jieba.analyse.textrank(content, withWeight=True,topK=20):
    print("%s %s" % (x, w))


#print(content)
#jieba.analyse.set_idf_path("path")
tags = jieba.analyse.extract_tags(content, withWeight=True)
#print("关键词："+"/".join(tags))
for tag in tags:
    print(tag[0]+tag[1])