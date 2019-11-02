import itchat
import requests


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'  # 自动回复的消息条数有限
    data = {
        'key': 'api',  # Tuling Key
        'info': msg,  # 这是发出去的消息
        'userid': 'robot'
    }
    # 通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')


# 用于接收来自朋友间的对话消息  #如果不用这个，朋友发的消息便不会自动回复
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return get_response(msg['Text'])


@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
# 用于接收群里面的对话消息
def print_content(msg):
    return get_response(msg['Text'])


itchat.auto_login(True)
itchat.run()