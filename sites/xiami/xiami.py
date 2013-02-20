# coding=utf8
# python 2.6+
# www.xiami.com
import sys
sys.path.append('../../libs')
from xcron import *
import time

class Xiami(XCron):
    def __init__(self):
        XCron.__init__(self)
        self.http = XHttp()

    # 登录
    def login(self):
        loginUrl = "http://www.xiami.com/member/login"
        loginData = {'done': "/", 'email': self.username, 'password': self.password, 'submit': "登 录"}
        headers = {'Referer':'http://www.xiami.com/', 'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:18.0) Gecko/20100101 Firefox/18.0 FirePHP/0.7.1'}
        result = self.http.request(loginUrl, loginData, headers)
        print result.info()

    # 签到
    def checkin(self):
        checkinUrl = "http://www.xiami.com/task/signin"
        checkinData = {}
        checkinHeaders = {'Referer':'http://www.xiami.com/', 'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:18.0) Gecko/20100101 Firefox/18.0 FirePHP/0.7.1'}
        checkinResult = self.http.request(checkinUrl, checkinData, checkinHeaders)
        print checkinResult.info()

xiami = Xiami()
print time.time()
xiami.login()
xiami.checkin()
