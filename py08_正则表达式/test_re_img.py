import re


def test_re_img():
    with open('img.html', encoding='utf-8') as f:
        html = f.read()
        # print(html)
        p = re.compile(r'<img.+?src=\"(.+?)\".+?>')
        list_img = p.findall(html)
        print(len(list_img))
        for ls in list_img:
            print(ls.replace('&amp;', '&'))


if __name__ == '__main__':
    test_re_img()
