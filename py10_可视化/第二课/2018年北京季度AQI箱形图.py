import pandas as pd
from pyecharts import Boxplot

df = pd.read_csv('D:/data/beijing_AQI_2018.csv')
dom = df[['Date', 'AQI']]
data = [[], [], [], []]
dom1, dom2, dom3, dom4 = data
for i,j in zip(dom['Date'], dom['AQI']):
    time = i.split('/')[1]    # 截取到月份
    if time in ['1', '2', '3']:
        dom1.append(j)
    elif time in ['4', '5', '6']:
        dom2.append(j)
    elif time in ['7', '8', '9']:
        dom3.append(j)
    else:
        dom4.append(j)

boxplot = Boxplot("2018年北京季度AQI走势箱形图", title_pos='center',
                  title_top='18', width=800, height=400)
x_axis = ['第一季度', '第二季度', '第三季度', '第四季度']
y_axis = [dom1, dom2, dom3, dom4]
_yaxis = boxplot.prepare_data(y_axis)
boxplot.add("", x_axis, _yaxis)
boxplot.render('2018年北京季度AQI箱形图.html')