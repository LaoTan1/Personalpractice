import requests  # 用rquests库做网络爬取
from bs4 import BeautifulSoup  # 用beautifusoup4做数据解析、分析
import numpy as np  # 用numpy对 n 维数组和矩阵进行运算
import matplotlib.pyplot as plt  # 用matplotlib做图表

allUniv = []  # 用于创建一个包含一条条大学排名的列表


def getHTMLText(url):  # 网络函数
    try:
        r = requests.get(url, timeout=30)  # 请求超时时间为30秒 （ url: 需要爬取的网站地址）
        r.raise_for_status()  # 如果状态不是200，则引发异常
        r.encoding = 'utf-8'  # 修改编码方式为utf-8
        return r.text
    except:
        return ""


# 观察源码发现我们想要的数据在<tr>下的<td>标签中的
def fillUnivList(soup):  # 数据获取函数
    data = soup.find_all('tr')  # name 参数可以查找所有名字为 tr 的tag
    for tr in data:
        ltd = tr.find_all('td')  # 解析tr中所有的td标签的文本
        if len(ltd) == 0:  # 这里是因为源码中还有其他的tr标签，但是没有td标签，所以可以筛选一下
            continue
        singleUniv = []  # 单个大学的排名信息
        for td in ltd:
            singleUniv.append(td.string)  # 提取td标签中的内容
        allUniv.append(singleUniv)
    return len(allUniv)


def printUnivList(num):  # 数据展示函数，输出大学排名表格，num 代表前多少名
    print("{0:^4}\t{1:^20}\t{2:^5}\t{3:^8}\t{4:^8}\t{5:^8}\t{6:^8}".format("排名", "学校名称", "省市", "总分", "生源质量", "培养结果",
                                                                           "顶尖成果"))
    for i in range(num):
        u = allUniv[i]
        if u[2] == "广东":
            print("{0:^4}\t{1:^20}\t{2:^5}\t{3:^8}\t{4:^8}\t{5:^8}\t{6:^8}".format(u[0], u[1], u[2], u[3], str(u[4]),
                                                                                   str(u[5]), str(u[9])))


def drawBarChart(num):
    zsdx = []
    hnlg = []
    nfkj = []
    for i in range(num):
        u = allUniv[i]  # 单独一条大学排名信息
        if u[1] == "中山大学":
            zsdx.append(float(u[3]))
            zsdx.append(float(u[4]))
            zsdx.append(float(str(u[5]).replace('%', '')))
            zsdx.append(float(u[9]))
        if u[1] == "华南理工大学":
            hnlg.append(float(u[3]))
            hnlg.append(float(u[4]))
            hnlg.append(float(str(u[5]).replace('%', '')))
            hnlg.append(float(u[9]))
        if u[1] == "南方科技大学":
            nfkj.append(float(u[3]))
            nfkj.append(float(u[4]))
            nfkj.append(float(str(u[5]).replace('%', '')))
            nfkj.append(float(u[9]))
    name_list = ['总分', '生源质量', '培养结果', "顶尖成果"]
    x = list(range(len(name_list)))
    total_width, n = 0.8, 4
    width = total_width / n
    fig, ax = plt.subplots()
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.bar(x, zsdx, width=width, label='中山大学', tick_label=name_list, fc='r')
    for i in range(len(x)):
        x[i] = x[i] + width
    plt.bar(x, hnlg, width=width, label='华南理工大学', fc='y')
    for i in range(len(x)):
        x[i] = x[i] + width
    plt.bar(x, nfkj, width=width, label='南方科技大学', fc='b')
    # plt.xticks(np.arange(len(name_list)))
    plt.legend()
    plt.show()


def drawBar(num):
    djcg = []
    name = []
    explode = []
    for i in range(num):
        u = allUniv[i]
        if u[2] == "广东":
            djcg.append(u[9])
            name.append(u[1])
            if u[1] == "中山大学":
                explode.append(0.5)
            else:
                explode.append(0)
    plt.rcParams['font.sans-serif'] = 'SimHei'
    fig1, ax1 = plt.subplots()
    ax1.pie(djcg, explode=explode, labels=name, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.legend()
    plt.show()


def main():  # 主函数测试
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    num = fillUnivList(soup)
    printUnivList(num)
    drawBarChart(num)
    drawBar(num)


if __name__ == '__main__':
    main()
