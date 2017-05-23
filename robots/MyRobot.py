# -*- coding: utf8 -*-
__author__ = 'ben'
import logging
from itchat.content import *
import requests
import itchat, time
logger = logging.getLogger('MyRobot')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


class TuLingReply(object) :
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    KEY = '8edce3ce905a4c1dbb965e6b35c3834d'
    def __init__(self):
        super(TuLingReply, self).__init__()

    def reply(self,msg):
        try:
            data = {
                'key'    : self.KEY,
                'info'   : msg,
                'userid' : 'wechat-robot',
            }
            r = requests.post(self.apiUrl, data=data)
            # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
            if r.status_code == requests.codes.ok:
                result = r.json()
                text = result.get('text')
                reply = text
                url = result.get('url')
                if url:
                    reply += "\n\t"+url

                list = result.get("list",[])
                for ele in list:
                    reply+="\n\t"+"%s(%s):%s" %(ele.get("article"),ele.get("source"),ele.get("detailurl"))
                return reply

            else:
                logger.error(r.text())
            # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
            # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
        except Exception,e:
            # 将会返回一个None
            logger.error(str(e))
            return

class MyReply(object):
    online =True
    nickName = u"当时汗就来了"
    tuLing = TuLingReply()
    def __init__(self):
        super(MyReply, self).__init__()

    def __get_ip(self):
        resp = requests.get("https://api.ipify.org?format=json")
        if resp.status_code == requests.codes.ok:
            result = resp.json()
            return result["ip"]
    def reply(self,msg):
        text = msg["Text"]
        if text == "ip":
            return self.__get_ip()
        elif text == "up":
            self.online = True
            return "success"
        elif text == "down":
            self.online = False
            return "success"
        else:
            return self.tuLing.reply(msg['Text'])

    def isMySelf(self,msg):

        return msg["User"].get("NickName") == self.nickName

tuLing = TuLingReply()
myRobot = MyReply()

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    logger.info("online %s" % myRobot.online)
    #logger.info(json.dumps(msg).decode("unicode_escape"))
    if myRobot.isMySelf(msg) :
        return myRobot.reply(msg)
    elif myRobot.online:
        defaultReply = u"暂时离线状态,如有急事请尝试其他联系方式"
        # 如果图灵Key出现问题，那么reply将会是None
        reply = tuLing.reply(msg['Text'])
        # a or b的意思是，如果a有内容，那么返回a，否则返回b
        # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
        reply = u"🤖:%s"% (reply or defaultReply)
        return reply
        #itchat.send(reply,msg["User"]["UserName"])

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

"""
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])
"""
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        level=logging.INFO,
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='../logs/robot.log',
        filemode='a'
    )
    itchat.auto_login(hotReload=True)
    itchat.run()
    #itchat.set_logging(showOnCmd=True,loggingFile="robot.log",loggingLevel=logging.DEBUG)


