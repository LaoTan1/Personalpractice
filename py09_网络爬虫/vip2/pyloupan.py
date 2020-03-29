import requests
import time
from lxml import html
from pymongo import MongoClient


# 获取某市区域的所有链接
def get_areas(url, col):
    print('start grabing areas')
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
                      Chrome/63.0.3239.108 Safari/537.36'}
    res = requests.get(url, headers=headers)
    content = html.fromstring(res.text)
    areas = content.xpath('//div[@class="filter-by-area-container"]/ul[@class="district-wrapper"]/li/text()')
    print(areas)
    areas_link = content.xpath('//div[@class="filter-by-area-container"]/ul[@class="district-wrapper"]/li/@data-district-spell')
    print(areas_link)
    for i in range(0, len(areas)):
        area = areas[i]
        area_link = areas_link[i]
        print(area_link)
        link = url+area_link
        print("开始抓取页面:"+link)
        get_pages(area, link, col)


#通过获取某一区域的页数，来拼接某一页的链接
def get_pages(area, area_link, col):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
    res = requests.get(area_link, headers=headers)
    content = html.fromstring(res.text)
    #链家新房页面统计每个区域的楼盘个数
    count = int(content.xpath('//div[@class ="page-box"]/@data-total-count')[0])
    #转换成页面，获取每个页面的楼盘信息
    if count%10 :
        pages = count//10+1
    else:
        pages = count//10
    print("这个区域有" + str(pages) + "页")

    for page in range(1, pages+1):
        url = area_link+'/pg' + str(page)+'/#'+area
        print("开始抓取" + str(page) +"的信息")
        get_house_info(area, url, col)


#获取某一区域某一页的详细房租信息
def get_house_info(area, url, col):
    hlist = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
         Chrome/63.0.3239.108 Safari/537.36'}
    time.sleep(2)
    try:
        print(url)
        res = requests.get(url, headers=headers)
        content = html.fromstring(res.text)

        for i in range(10):
            try:
                title = content.xpath("//ul[@class='resblock-list-wrapper']/li/a/@title")[i]
                print(title)
                detail_area= content.xpath("//ul[@class='resblock-list-wrapper']/li//div[@class='resblock-location']/span[2]/text()")[i]
                print(detail_area)
                detail_place = content.xpath("//ul[@class='resblock-list-wrapper']/li//div[@class='resblock-location']/a/text()")[i]
                print(detail_place)
                type = content.xpath("//ul[@class='resblock-list-wrapper']/li//div[@class='resblock-name']/span[1]/text()")[i]
                print(type)
                try:
                    square = content.xpath("//ul[@class='resblock-list-wrapper']/li//div[@class='resblock-area']/span/text()")[i]
                except Exception as e:
                    square = ""
                print(square)
                price = content.xpath("//ul[@class='resblock-list-wrapper']/li//div[@class='main-price']/span[1]/text()")[i]
                #价格待定的楼盘设置price为0
                if price=='价格待定':
                    price = 0
                print(price)
                item = {
                    "area": area,
                    "title": title,
                    "type": type,
                    "square": square,
                    "detail_area": detail_area,
                    "detail_place": detail_place,
                    "price": int(price),
                }
                hlist.append(item)
            except Exception as e:
                break
        print('writing work has done!continue the next page')
        col.insert(hlist)
    except Exception as e:
        print(res.text)
        print(url)
        print( 'ooops! connecting error, retrying.....')
        time.sleep(20)


def main():
    print('start!')
    url = 'https://wh.fang.lianjia.com/loupan/'
    client = MongoClient('localhost', 27017)
    db = client.get_database("lianjia")
    col = db.get_collection("loupan")
    get_areas(url, col)


if __name__ == '__main__':
    main()