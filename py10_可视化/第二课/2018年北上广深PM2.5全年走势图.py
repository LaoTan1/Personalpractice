import numpy as np
import  pandas as pd
from pyecharts import Line

citys = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
cityes_PM = []
for i in range(4):
    filename ='D:/data/'+ citys[i] + '_AQI' + '_2018.csv'
    api_data = pd.read_csv(filename)

    get_data = api_data[['Date', 'PM']]
    month_for_data = []
    for j in get_data['Date']:
        time = j.split('/')[1]
        month_for_data.append(time)
    api_data['Month'] = month_for_data  # 获取每行数据的月份

    # 求每个月PM2.5平均值
    month_data = api_data.groupby(['Month'])
    month_PM = month_data['PM'].agg(['mean'])
    month_PM.reset_index(inplace=True)
    month_PM_average = month_PM.sort_index()

    # 获取每个城市每个月PM的数据，转化为int数据类型
    month_PM_data = np.array(month_PM_average['mean'])
    month_PM_data_int = ["{}".format(int(i)) for i in month_PM_data]
    cityes_PM.append(month_PM_data_int)

months = ["{}".format(str(i) + '月') for i in range(1, 13)]

line = Line("2018年北上广深PM2.5全年走势图", title_pos='center', title_top='0', width=800, height=400)
line.add("北京", months, cityes_PM[0], line_color='red', legend_top='8%')
line.add("上海", months, cityes_PM[1], line_color='purple', legend_top='8%')
line.add("广州", months, cityes_PM[2], line_color='blue', legend_top='8%')
line.add("深圳", months, cityes_PM[3], line_color='orange', legend_top='8%')
line.render("2018年北上广深PM2.5全年走势图.html")