import urllib.request
import re
import mysql.connector


def crawl_site(url):
    for page in range(997, 1000):
        pg_url = '{}{}.html'.format(url, page)
        html = download(pg_url)
        if html is None:
            break
        else:
            pt = r'<div class="read_ny fontcontent ">(.*?)</div>'
            c = re.findall(pt, html)
            conn = mysql.connector.connect(
                host="localhost", port="3306",
                user="root", password="1224",
                database="text"
            )
            cur = conn.cursor()
            for t in c:
                t = re.sub(r'<.*?>', "", t)
                t = re.sub(r'</.*?>', "", t)
                t = re.sub(r'&nbsp;', "", t)
                cur.execute("insert into tnews(ccontend) values('" + t + "')")
                conn.commit()
                print(t)
            cur.close()
            conn.close()


def download(url):
    print("Downloading:", url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', "xjh")
    fp = urllib.request.urlopen(request);
    html = fp.read().decode()
    return html


crawl_site("http://dqxx.baiyunu.edu.cn/html/cn/xydt/22_17.html")
