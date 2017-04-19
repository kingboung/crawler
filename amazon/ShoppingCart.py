from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/home-garden-kitchen-furniture-bedding/b/ref=topnav_storetab_hg?ie=UTF8&node=1055398')
wait = WebDriverWait(driver,2)
elem = wait.until(EC.presence_of_element_located((By.ID,'twotabsearchtextbox')))
elem.clear()
elem.send_keys('Travel-Size Humidifiers')
elem.send_keys(Keys.RETURN)
indexGood = 'Handheld USB Misting Fan,Rechargeable Water Spray Fan Desktop Mini Humidifier for Home Office and Travel (Pink)'
while True:
    if indexGood in driver.page_source:
        driver.find_element_by_xpath('//*[@title="Handheld USB Misting Fan,Rechargeable Water Spray Fan Desktop Mini Humidifier for Home Office and Travel (Pink)"]').click()
        wait.until(EC.presence_of_element_located((By.ID,'buybox-see-all-buying-choices-announce')))
        driver.find_element_by_id('buybox-see-all-buying-choices-announce').click()
        wait.until(EC.presence_of_element_located((By.NAME,'submit.addToCart')))
        driver.find_element_by_name('submit.addToCart').click()
        break
    else:
        driver.find_element_by_xpath('//*[@id="pagnNextString"]').click()
