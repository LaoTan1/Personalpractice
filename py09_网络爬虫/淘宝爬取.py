# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

import requests
import re


def get_HTML_Text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text

    except Exception as e:
        print(e)


def parse_page(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            ilt.append([title, price])
            return ilt
    except Exception as e:
        print(e)


def print_magss(list_text):
    tepl = "{:4}\t{:16}\t{:8}"
    print(tepl.format("序号", "商品名称", "价格"))
    g = 0
    for i in list_text:
        count = g + 1
        print(list_text.format(count, i[1], i[0]))


def main():
    goods = "书包"
    page = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    list_text = []
    for i in range(page):
        try:
            url = start_url + "&s=" + str(44 * i)
            html = get_HTML_Text(url)
            parse_page(list_text, html)
        except:
            continue
    print_magss(list_text)


main()
