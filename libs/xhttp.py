# coding=utf8
import urllib,urllib2

class XHttp:
    def __init__(self):
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        urllib2.install_opener(opener)
        pass

    def request(self, url, data = '', headers = {}):
        try:
            # register cookie handler
            data = urllib.urlencode(data)
            request = urllib2.Request(url, data, headers)
            url = urllib2.urlopen(request)
        except urllib2.HTTPError:
            pass
        except Exception, e:
            print e
            exit()
        return url
