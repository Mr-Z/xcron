# coding=utf8
# python 2.6+
# www.xiami.com
import sys
sys.path.append('../../libs')
from xcron import *

class Xiami(XCron):
    def __init__(self):
        XCron.__init__(self)
        self.http = XHttp()

    # 登录
    def login(self):
        loginUrl = "http://www.xiami.com/member/login"
        loginData = {'done': "/", 'email': self.username, 'password': self.password, 'submit': "登 录"}
        result = self.http.request(loginUrl, loginData)
        print result.info()

    # 签到
    def checkin(self):
        checkinUrl = "http://www.xiami.com/task/signin"
        checkinData = {}
        checkinHeaders = {'Referer':'http://www.xiami.com/'}
        checkinResult = self.http.request(checkinUrl, checkinData, checkinHeaders)
        print checkinResult.info()

xiami = Xiami()
xiami.login()
xiami.checkin()
