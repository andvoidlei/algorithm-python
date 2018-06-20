# coding:utf-8
from FPG import test03

oneDimList = []


def loadSimpDat():
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat

#sdfkjsldkjflsdf
# 数据准备
simpDat = loadSimpDat()
for list in simpDat:
    oneDimList += list
# 建header table
headerTable = test03.HeaderTable().create(oneDimList, 3)
# 建FP tree
buildTree = test03.BuildTree()
updDat = buildTree.refactor(simpDat, headerTable)
print(updDat)
fpTree = buildTree.update(updDat)
# 打印结果
for fpTreeItem in fpTree:
    print(    'parent:' + fpTreeItem.parent + ', name:' + fpTreeItem.name + \
    ', num:' + str(fpTreeItem.numOccur))