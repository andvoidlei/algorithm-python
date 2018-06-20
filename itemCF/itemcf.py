# -*- coding:utf-8 -*-

import math

# ItemCF算法
def ItemSimilarity(train):
    C = dict()
    N = dict()
    for u,items in train.items():
        for i in items.keys():
            N[i] += 1
            for j in items.keys():
                if i == j:
                    continue
                C[i][j] += 1
    W = dict()
    for i,related_items in C.items():
        for j,cij in related_items.items():
            W[i][j] = cij / math.sqrt( N[i] * N[j])
    return W

# ItemCF-IUF算法
def ItemSimilarity_v2(train):
    C = dict()
    N = dict()
    for u,items in train.items():
        for i in items.keys():
            N[i] += 1
            for j in items.keys():
                if i == j:
                    continue
                C[i][j] += 1 / math.log(1+len(items)*1.0)
    W = dict()
    for i,related_items in C.items():
        for j,cij in related_items.items():
            W[i][j] = cij / math.sqrt( N[i] * N[j])
    return W

def Recommend(train,user_id,W,K):
    rank = dict()
    ru = train[user_id]
    for i,pi in ru.items():
        for j,wj in sorted(W[i].items,key=itemgetter(1),reverse=True)[0:K]:
            if j in ru:
                continue
            rank[j] += pi*wj
    return rank