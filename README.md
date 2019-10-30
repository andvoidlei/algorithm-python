# algorithm-python
基于python的算法实例

## 第一部分  决策树
决策树算法是一种分类算法。对待一个数据，决策树使用多个决策判断确定最终的分类，举个小例子说明一下：给定一个动物，判断什么动物的分类，首先“它是哺乳类动物吗？”，如果不是，“它是陆地动物吗？”，如果不是，“是空中动物吗？”……以此类推，最终判断动物的分类，确定动物。

### 熵
熵代表一个系统的杂乱程度，熵越大，系统越杂乱。对一个数据集中数据的分类就是使得该数据集熵减小的过程。

信息熵为信息的期望值，熵是用来度量随机变量的不确定性。数学公式表达如下：

```math
H\left ( X \right )= \sum_{i=1}^{n}p\left ( x_{i} \right )I\left ( x_{i} \right )=-\sum_{i=1}^{n}p\left ( x_{i} \right )log_{b} p\left ( x_{i} \right )
```
其中负号是用来保证信息量是正数或者零。H(X)就被称为随机变量x的熵，它是对所有可能发生的事件产生的信息量的期望。从公式可以得出结论：随机变量的取值个数越多，状态数也就越多，信息熵就越大，不确定性就越大。

### 第一步  熵计算
一个简单的例子  
下表包含5个海洋动物，特征包括：不浮出水面是否可以生存，以及是否有脚蹼。将这些动物分为两类：鱼类和非鱼类。要研究的问题就是依据第一个特征还是第二个特征划分数据。

id | 不浮出水面是否可以生存	 | 是否有脚蹼	|属于鱼类
---|---|---|---
1|	是|	是|	是
2|	是|	是|	是
3|	是|	否|	否
4|	否|	是|	否
5|	否|	是|	否

熵的计算代码
```

def cal_entropy(data):
    '''计算样本实例的熵'''
    entries_num = len(data)
    label_count = {} #字典存储每个类别出现的次数
 
    for vec in data:
        cur_label = vec[-1] 
    # 将样本标签提取出来，并计数
        label_count[cur_label] = label_count.get(cur_label,0) + 1
    Entropy = 0.0
    # 对每一个类别，计算样本中取到该类的概率
    # 最后将概率带入，求出熵
    for key in label_count:
        prob = float(label_count[key]) / entries_num
        Entropy += prob * math.log(prob, 2)
    return (0-Entropy)
```
[项目代码](https://github.com/andvoidlei/algorithm-python/blob/master/decision-tree/cal_entropy.py)
