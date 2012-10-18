# coding=utf8
from xhttp import *
import ConfigParser

class XCron:
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open('config.ini'))
        self.username = config.get("userinfo","username")
        self.password = config.get("userinfo","password")
