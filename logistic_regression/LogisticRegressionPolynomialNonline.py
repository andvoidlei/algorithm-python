"""
    对ex2data2.txt中的数据进行逻辑回归（引入多项式特征）
"""
from sklearn.model_selection import train_test_split
from matplotlib.colors import ListedColormap
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 数据格式：成绩1,成绩2,是否被录取（1代表被录取，0代表未被录取）


# 函数定义
def plot_decision_boundary(model, axis):
    x0, x1 = np.meshgrid(
        np.linspace(axis[0], axis[1], int((axis[1] - axis[0]) * 100)).reshape(-1, 1),
        np.linspace(axis[2], axis[3], int((axis[3] - axis[2]) * 100)).reshape(-1, 1),
    )
    X_new = np.c_[x0.ravel(), x1.ravel()]

    y_predict = model.predict(X_new)
    zz = y_predict.reshape(x0.shape)

    custom_cmap = ListedColormap(['#EF9A9A', '#FFF59D', '#90CAF9'])

    plt.contourf(x0, x1, zz, cmap=custom_cmap)


def PolynomialLogisticRegression(degree):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('std_scaler', StandardScaler()),
        ('log_reg', LogisticRegression())
    ])


# 读取数据
data = np.loadtxt('../data/ex2data2.txt', delimiter=',')
data_X = data[:, 0:2]
data_y = data[:, 2]

# 数据分割
X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, random_state=666)

# 训练模型
poly_log_reg = PolynomialLogisticRegression(degree=2)
poly_log_reg.fit(X_train, y_train)

# 结果可视化
plot_decision_boundary(poly_log_reg, axis=[-1, 1, -1, 1])
plt.scatter(data_X[data_y == 0, 0], data_X[data_y == 0, 1], color='red')
plt.scatter(data_X[data_y == 1, 0], data_X[data_y == 1, 1], color='blue')
plt.xlabel('成绩1')
plt.ylabel('成绩2')
plt.title('两门课程成绩与是否录取的关系')
plt.show()

# 模型测试
print(poly_log_reg.score(X_train, y_train))
print(poly_log_reg.score(X_test, y_test))