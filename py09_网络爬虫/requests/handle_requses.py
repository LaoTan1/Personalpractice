# import requests
#
# data = {"name": "imooc"}
# response = requests.post(url="http://www.qq.com", data=data)
# print(response.text)

#
# import requests
#
# response = requests.get("http://www.imooc.com/static/img/index/logo.png")
# with open('imooc.png', 'wb') as f:
#     f.write(response.content)
#
#
# import requests
#
# response = requests.get("http://httpbin.org/ip")
# data = response.json()
# print(data)
# print(data['origin'])


import requests

response = requests.get("http://github.com", timeout=9)
print(response.text)
print(response.status_code)
print(response.request.headers)
