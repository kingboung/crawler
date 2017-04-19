from selenium import webdriver

from http import cookiejar
from urllib import request, parse

url = 'https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&prevRID=RP1Y9432K1R4TK9QQ07V&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'
regurl = 'https://www.amazon.com/ap/register'

driver = webdriver.PhantomJS()
driver.get(url)

post_dict = {
    'appActionToken':'',
    'appAction':'REGISTER',
    'openid.pape.max_auth_age':'',
    'openid.return_to':'',
    'prevRID':'',
    'openid.identity':'',
    'openid.assoc_handle':'',
    'openid.mode':'',
    'openid.ns.pape':'',
    'failedSignInCount':'',
    'openid.claimed_id':'',
    'pageId':'',
    'openid.ns':'',
    'claimToken':'',
    'customerName':'Judices',
    'email':'Judices123@126.com',
    'password':'123456',
    'passwordCheck':'123456',
    'metadata1':''
}

missKey = ['customerName','email','password','passwordCheck']

for key in post_dict.keys():
    if key not in missKey:
        elem = driver.find_element_by_name(key)
        value = elem.get_attribute('value')
        post_dict[key] = value

cookie = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
proxy_support = request.ProxyHandler({'sock5':'localhost:1080'})
opener = request.build_opener(handler)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
req = request.Request(regurl, data=parse.urlencode(post_dict).encode('utf-8'), headers=headers)

print(post_dict)

with opener.open(req) as f:
    with open('c.html', 'wb') as html:
        html.write(f.read())