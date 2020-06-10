import numpy as np
import pandas as pd
from pyecharts import Line

citys = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
cityes_AQI = []
for i in range(4):
    filename ='D:/data/'+ citys[i] + '_AQI' + '_2018.csv'
    aqi_data = pd.read_csv(filename)

    get_data = aqi_data[['Date','AQI']]
    month_for_data = []
    for j in get_data['Date']:
        time = j.split('/')[1]
        month_for_data.append(time)
    aqi_data['Month'] = month_for_data
#AQI平均值
    month_data = aqi_data.groupby(['Month'])
    month_AQI = month_data['AQI'].agg(['mean'])
    month_AQI.reset_index(inplace=True)
    month_AQI_average = month_AQI.sort_index()
    month_AQI_data = np.array(month_AQI_average['mean'])
    month_AQI_data_int = ["{}".format(int(i)) for i in month_AQI_data]
    cityes_AQI.append(month_AQI_data_int)

months = ["{}".format(str(i) + '月') for i in range(1,13)]

line = Line("2018年北上广深AQI全年走势图", title_pos='center', title_top='0', width=800, height=400)
line.add("北京", months, cityes_AQI[0], line_color='red', legend_top='8%')
line.add("上海", months, cityes_AQI[1], line_color='purple', legend_top='8%')
line.add("广州", months, cityes_AQI[2], line_color='blue', legend_top='8%')
line.add("深圳", months, cityes_AQI[3], line_color='orange', legend_top='8%')
line.render("2018年北上广深AQI全年走势图.html")