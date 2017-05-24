import logging
import itchat
import sys
import robots.MyRobot
__author__ = 'ben'

reload(sys)
sys.setdefaultencoding('utf8')
logging.basicConfig(
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    level=logging.INFO,
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='./logs/robot.log',
    filemode='a'
)

itchat.auto_login(hotReload=True,enableCmdQR=True)
itchat.run()


