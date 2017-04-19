from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class amazon(object):

    def __init__(self, name, email, password):

        PROXY = '127.0.0.1:1080'

        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            'httpProxy':PROXY,
            "ftpProxy": PROXY,
            "sslProxy": PROXY,
            "noProxy": None,
            "proxyType": "MANUAL",
            "class": "org.openqa.selenium.Proxy",
            "autodetect": False
        }

        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,2)
        self.name = name
        self.email = email
        self.password = password
        self.result = ''

    def register(self):
        regURL = 'https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&prevRID=RP1Y9432K1R4TK9QQ07V&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'
        self.driver.get(regURL)
        elem = self.wait.until(EC.presence_of_element_located((By.NAME, 'customerName')))
        elem.clear()
        elem.send_keys(self.name)
        elem = self.driver.find_element_by_name('email')
        elem.clear()
        elem.send_keys(self.email)
        elem = self.driver.find_element_by_name('password')
        elem.clear()
        elem.send_keys(self.password)
        elem = self.driver.find_element_by_name('passwordCheck')
        elem.clear()
        elem.send_keys(self.password)
        self.driver.find_element_by_id('continue').click()
        if 'Online Shopping' in self.driver.title:
            self.addToShoppingCart()
            self.result = 'success'
        else:
            self.result = 'fail'
            self.driver.quit()

    def addToShoppingCart(self):
        select = Select(self.driver.find_element_by_id('searchDropdownBox'))
        select.select_by_visible_text('Home & Kitchen')
        elem = self.wait.until(EC.presence_of_element_located((By.ID,'twotabsearchtextbox')))
        elem.clear()
        elem.send_keys('Travel-Size Humidifiers')
        elem.send_keys(Keys.RETURN)
        indexGood = 'Handheld USB Misting Fan,Rechargeable Water Spray Fan Desktop Mini Humidifier for Home Office and Travel (Pink)'
        while True:
            if indexGood in self.driver.page_source:
                self.driver.find_element_by_xpath('//*[@title="Handheld USB Misting Fan,Rechargeable Water Spray Fan Desktop Mini Humidifier for Home Office and Travel (Pink)"]').click()
                self.wait.until(EC.presence_of_element_located((By.ID,'buybox-see-all-buying-choices-announce')))
                self.driver.find_element_by_id('buybox-see-all-buying-choices-announce').click()
                self.wait.until(EC.presence_of_element_located((By.NAME,'submit.addToCart')))
                self.driver.find_element_by_name('submit.addToCart').click()
                self.driver.quit()
                break
            else:
                self.driver.find_element_by_xpath('//*[@id="pagnNextString"]').click()


if __name__ == '__main__':

    print('----------------------自动注册并添加购物车---------------------')
    name = 'Jack'
    password = '123456'
    index = 0
    successCount = 0
    while True:
        if successCount == 500:
            print('完成500用户的注册、添加任务~~~')
        email = 'Jack' + str(index) + '@126.com'
        print('注册用户%d:  用户名 %s  邮箱 %s  密码 %s' % (index, name, email, password))
        instance = amazon(name, email, password)
        instance.register()
        index += 1
        if instance.result is 'success':
            print('注册、添加成功')
            print()
            successCount+=1
        else:
            print('注册失败')
            print()