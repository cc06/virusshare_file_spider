# coding=utf-8
#author='CX-15'
'''
    please check the username and password first

'''
import urllib
import urllib2
import cookielib
import datetime
import time
import re

url = 'http://www.virusshare.com'
def Get_Page():

    #主机地址
    hosturl = 'http://virusshare.com/'
    # post的url
    posturl = 'http://virusshare.com/processlogin.4n6'
   #设置cookie处理器
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    #打开登陆页面
    h = urllib2.urlopen(hosturl)
    #构造header
    headers = {'User-Agent': 'Mozilla/4.0 compatible; MSIE 5.5; Windows NT'}

    postData = {'username': '*****',
                'password': '*****'
    }
    #给post数据编码
    postData = urllib.urlencode(postData)
    #通过urllib提供的request方法向指定的url发送刚才构造的数据，完成登陆
    request = urllib2.Request(posturl, postData, headers)
    # print request
    response = urllib2.urlopen(request)
    text = response.read()
    return text


def Judje_Page(page):
    '''
    判断是不是PE文件，如果是，保存到本地，如果不是则丢弃！
    '''
    PE_page = re.search('PE', page)

    if PE_page:
        SHA256 = re.findall(r'href="(.*?)">', page)
        url = 'http://virusshare.com/'+ SHA256[9]
        print '\033[0;32;40m'+'匹配成功! ',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'-------现在保存文件.....'
        # print url
        #将文件下载并保存到本地
        i = str(SHA256[9])
        with open(str(i[-64:])+'.exe','wb')as code:
            code.write(urllib2.urlopen(url).read())
    else:
        print '\033[0;31;40m'+'匹配失败！',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'-------现在丢弃文件.....'

while True:
    page = Get_Page()
    # print page
    Judje_Page(page)
    time.sleep(15)


