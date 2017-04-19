from urllib import request, parse
from http import cookiejar
import re


url = 'https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&prevRID=RP1Y9432K1R4TK9QQ07V&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'

regurl = 'https://www.amazon.com/ap/register'

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

cookie = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
proxy_support = request.ProxyHandler({'sock5':'localhost:1080'})
opener = request.build_opener(proxy_support, handler)

# req = request.Request(url)

with opener.open(url) as f:
    file = f.read()
    lines = str(file, encoding='utf-8').split('\n')
    for line in lines:
        for key in post_dict.keys():
            if key in line and 'value' in line:
                value = re.search(r'value=\"[a-zA-Z0-9\:\=\/]+\"', line).group()[7:-1]
                post_dict[key] = value

print(post_dict)


# req = request.Request(regurl, data=parse.urlencode(post_dict).encode('utf-8'))
# req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')

with opener.open(regurl, data=parse.urlencode(post_dict).encode('utf-8')) as f:
    with open('c.html', 'wb') as html:
        html.write(f.read())
