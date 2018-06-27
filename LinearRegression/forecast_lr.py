# coding:utf-8
##############################################################
# create by wxl 20180107                                     #
# dt,year,mm,week_day,login_7d,active_cnt,order_amt          #
# 20150101,2015,1,5,45281,7545,2971102.7                     #
#                                                            #
#                                                            #
##############################################################

from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import sys




def get_train_data(file_name, v_source_day, v_day_after, v_predict_val):
    data = pd.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    Z_parameter = []
    reg_col = 'register_pre_' + v_day_after + 'd'
    act_col = 'active_cnt_' + v_day_after + 'd'
    # year mm week_day   register_cnt   active_cnt predict_val
    for order_date, year, mm, week_day, register_cnt, active_cnt, predict_val in zip(data['order_date'], data['year'],
                                                                                     data['mm'], data['week_day'],
                                                                                     data[reg_col], data[act_col],
                                                                                     data[v_predict_val]):
        if int(order_date) <= int(v_source_day):
            X_parameter.append([int(year), int(mm), int(week_day), int(register_cnt), int(active_cnt)])
            Y_parameter.append(float(predict_val))
    return X_parameter, Y_parameter


def get_predict_data(file_name, v_source_day, v_day_after, v_predict_val):
    data = pd.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    Z_parameter = []
    reg_col = 'register_pre_' + v_day_after + 'd'
    act_col = 'active_cnt_' + v_day_after + 'd'
    # year mm week_day   register_cnt   active_cnt predict_val
    for order_date, year, mm, week_day, register_cnt, active_cnt, predict_val in zip(data['order_date'], data['year'],
                                                                                     data['mm'], data['week_day'],
                                                                                     data[reg_col], data[act_col],
                                                                                     data[v_predict_val]):
        if int(order_date) > int(v_source_day):
            X_parameter.append([int(year), int(mm), int(week_day), int(register_cnt), int(active_cnt)])
            Y_parameter.append(float(predict_val))
            Z_parameter.append(float(order_date))
    return X_parameter, Y_parameter, Z_parameter


def forecast(in_file_name,day_after, in_day_id, in_predict_val):
    # file_name='./data-new.csv'
    file_name = in_file_name
    predict_type = in_predict_val
    day_id = in_day_id
    X, Y = get_train_data(file_name, day_id, day_after, predict_type)
    model = LinearRegression()
    model.fit(X, Y)

    X_test, y_test, z_test = get_predict_data(file_name, day_id, day_after, predict_type)
    file_nm_temp = '../data/order_predict-' + day_id + '_temp.csv'
    file_object = open(file_nm_temp, 'a+')
    predictions = model.predict(X_test)

    for i, prediction in enumerate(predictions):
        predict_day = z_test[i]
        predict_day_dt = datetime.datetime.strptime(str(int(predict_day)), '%Y%m%d')
        source_day = int((predict_day_dt - datetime.timedelta(days=int(day_after))).strftime('%Y%m%d'))

        if predict_type == 'orders_amt':
            ord_pred = 0
            ord_real = 0
            amt_pred = prediction
            amt_real = y_test[i]
        elif predict_type == 'orders_cnt':
            ord_pred = prediction
            ord_real = y_test[i]
            amt_pred = 0
            amt_real = 0
        else:
            ord_pred = 0
            ord_real = 0
            amt_pred = 0
            amt_real = 0

        # print('%d,%.2f,%d,%s,%s,%s' % (predict_day,prediction,orders_cnt, y_test[i],source_day,day_after))
        file_object.write(
            '%d,%d,%.2f,%d,%.2f,%d' % (predict_day, ord_pred, amt_pred, ord_real, amt_real, source_day) + '\n')
    print('R-squared: %.2f' % model.score(X_test, y_test))
    file_object.close


def forecast_day(day_after, in_day_id):
    file_name = '../data/order_data-' + in_day_id + '.csv'
    forecast(file_name,day_after, in_day_id, 'orders_amt')
    forecast(file_name,day_after, in_day_id, 'orders_cnt')


if len(sys.argv) <= 1:
    day_id = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')
else:
    day_id = sys.argv[1]
day_id='20180531'
file_name='../data/order_data-' + day_id + '.csv'
file_nm_temp = '../data/order_predict-' + day_id + '_temp.csv'

forecast_day('1', day_id)
forecast_day('2', day_id)
forecast_day('3', day_id)
forecast_day('4', day_id)
forecast_day('5', day_id)
forecast_day('6', day_id)
forecast_day('7', day_id)

# 汇总数据
data=pd.read_csv(file_name)
data_temp = pd.read_csv(file_nm_temp, header=0,
                        names=['predict_day', 'ord_pred', 'amt_pred', 'ord_real', 'amt_real', 'source_day'])
# data_gather=data_temp.groupby(['predict_day','source_day']).max()
# data_gather.to_csv('./data/order_predict-'+day_id+'.csv')


data_pred_day = data_temp[data_temp['source_day'] == int(day_id)][['predict_day','ord_pred','ord_real']]
#data_gather_day = data_temp.groupby(['predict_day', 'source_day']).max()
data_pred_day.to_csv('../data/order_predict-' + day_id + '.csv', header=False)


#关联获取真实值与与测试
a=data_pred_day[['predict_day','ord_pred']]
b=data[['order_date','orders_cnt']]
b.columns = ['data_date','orders_cnt']
a.columns =['data_date','ord_pred']
rst=pd.merge(b,a,how='left',on=['data_date'])
rst.loc[(rst['data_date'] > 20180501),['data_date','ord_pred','orders_cnt']].groupby('data_date').max().plot()
plt.show()