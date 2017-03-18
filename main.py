#-*- coding: UTF-8 -*- 
import requests
import json
import werobot

robot = werobot.WeRoBot(token='yourtoken')
appkey = ''
with open("key.txt",'r') as fi :
    appkey = fi.readline()

def tuling_auto_replay(uid, msg):
    url = "http://www.tuling123.com/openapi/api"
    user_id = uid.replace('@', '')[:30]
    body = {'key': appkey, 'info': msg, 'userid': user_id}
    r = requests.post(url, data=body)
    respond = json.loads(r.text)
    result = ''
    if respond['code'] == 100000:
        result = respond['text'].replace('<br>', '  ')
        result = result.replace(u'\xa0', u' ')
    elif respond['code'] == 200000:
        result = respond['url']
    elif respond['code'] == 302000:
        for k in respond['list']:
            result = result + u"[" + k['source'] + u"] " +\
            k['article'] + "\t" + k['detailurl'] + "\n"
    else:
        result = respond['text'].replace('<br>', '  ')
        result = result.replace(u'\xa0', u' ')
    return result

@robot.text
def echo(message):
    return tuling_auto_replay(message.FromUserName, message.content)

@robot.handler
def handler(message):
    return u'奴家目前只支持文字消息啦...'

@robot.subscribe
def subscribe(message):
    return u'''欢迎关注:世界很大也很美好。
当前公众号只有一个功能:与机器人对话，后续会加很多有意思的功能，敬请期待。
现在你可以跟它随便聊天，它会蠢萌的回复你。
还可以让他讲笑话、讲小故事、问它生活常识、问它星座运势、问它新闻、成语接龙、问菜谱、差快递、查天气、查列车|飞机航班、让他计算简单的算术运算、查日期、翻译英文等等
有些东西还是比较实用的呢，比较有意思的是讲笑话、小故事、成语接龙、翻译，快来试试吧。

''' 

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] =	1234 
robot.run()
