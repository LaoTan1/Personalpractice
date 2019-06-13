# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'Lfrom tkinter import '

from tkinter import *
from urllib.request import urlretrieve
from selenium import webdriver
import os

headers = {
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}


def song_load(item):
    song_id = item['song_id']
    song_name = item['song_name']
    song_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)

    # 创建一个文件夹
    # exist_ok=True 如果文件存在不会报错 不会继续创建
    os.makedirs('music_netease', exist_ok=True)
    path = 'music_netease\{}.mp3'.format(song_name)

    # 显示数据到文本框
    text.insert(END, '歌曲：{},正在下载...'.format(song_name))
    # 文本框滚动
    text.see(END)
    # 更新
    text.update()

    # 下载歌曲
    urlretrieve(song_url, path)

    text.insert(END, '下载完毕: {},请试听!'.format(song_name))
    text.see(END)
    text.update()


# 搜索歌曲名字
def get_music_name():
    # 获取输入框输入的歌曲名字
    name = entry.get()
    # 拼接url
    url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(name)
    print(url)
    # 搜索歌曲网页
    diver = webdriver.Chrome()
    diver.get(url=url)
    diver.switch_to.frame('g_iframe')

    # response = diver.find_element_by_xpath('./following-sibling::div//a/@href')
    # 获取歌曲id
    req = diver.find_element_by_id('m-search')
    a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute("href")
    print(a_id)
    song_id = a_id.split('=')[-1]
    print(song_id)

    # 获取歌曲名
    song_name = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//b').get_attribute("title")
    print(song_name)

    # 构建字典 id name
    item = {}
    item['song_id'] = song_id
    item['song_name'] = song_name

    print(item)

    diver.quit()  # 退出浏览器
    # diver.close()  # 退出当前页面

    # 下载歌曲
    song_load(item)


# 搭建界面

# 创建界面
root = Tk()
# 添加标题
root.title('网易云音乐')
# 设置窗口大小 x 小写x连，不能用乘号 后面两位是x,y坐标,固定初始位置
root.geometry('560x450+400+200')

# 标签控件
label = Label(root, text='请输入下载的歌曲：', font=('华文行楷', 20))
# 标签定位 grid 网格式定位
label.grid()  # 默认 row=0,column=0
# 输入框
entry = Entry(root, font=('隶书', 20))
# 定位 第0行 第1列
entry.grid(row=0, column=1)
# 列表框
text = Listbox(root, font=('楷书', 16), width=50, heigh=15)
# 定位 columnspan 组件横跨的列数
text.grid(row=1, columnspan=2)

# 点击按钮
button = Button(root, text='开始下载', font=('隶书', 15), command=get_music_name)
# 定位 sticky 对齐方式 W E N S  东南西北
button.grid(row=2, column=0, sticky=W)

# command 点击触发方法
button1 = Button(root, text='退出程序', font=('隶书', 15), command=root.quit)
# 定位 sticky 对齐方式 W E N S  东南西北
button1.grid(row=2, column=1, sticky=E)

# 显示界面
root.mainloop()
