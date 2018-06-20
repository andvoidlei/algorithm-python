# coding:utf-8
class HeaderTable:
    def __init__(self):
        pass

    def create(self, dat, minsup):
        headerTable = {}
        # 去重
        setDat = set(dat)
        # 计频繁数
        for key in setDat:
            headerTable[key] = dat.count(key)
            # 依据最小支持度去项
        for k, v in list(headerTable.items()):
            if v < minsup:
                del (headerTable[k])
                # 重排序
        headerTable = sorted(headerTable.items(), key=lambda i: i[1], reverse=True)
        return headerTable


class FPTreeItem:
    def __init__(self, key, name, numOccur, parent):
        self.key = key  # key
        self.name = name  # 项名
        self.numOccur = numOccur  # 频繁值
        self.parent = parent  # 父节点


class BuildTree:

    # inDat: (list) [[],[]]
    def refactor(self, inDat, headerTable):
        lineCounter = 0
        datLine = []
        dat = []

        # 依据headerTable去除小于最小支持度的项、重排序
        for list in inDat:
            lineCounter += 1
            for i in headerTable:
                if i[0] in list:
                    datLine.append(i[0])
            dat.append(datLine)
            datLine = []
        return dat

        # updDat: (list) [[],[]]

    def update(self, updDat):
        fpTree = []

        for list in updDat:
            parent = ''
            keyLink = ''
            for item in list:
                parent = keyLink
                keyLink += item
                for fpTreeItem in fpTree:
                    if keyLink == fpTreeItem.key:
                        # 相似元素项节点合并
                        fpTreeItem.numOccur += 1
                        break
                        # 没有这个元素项时创建一个新节点
                else:
                    fpTreeItem = FPTreeItem(keyLink, item, 1, parent)
                    fpTree.append(fpTreeItem)
        return fpTree