from selenium.webdriver import Chrome
import time
import os

url = "https://www.cathaybk.com.tw/cathaybk/personal/credit-card/cards/intro/list/"

# 開啟並取得國泰信用卡網頁。
driver = Chrome("./chromedriver.exe")
# 注意是否要放大，或自訂螢幕大小。
driver.maximize_window()
time.sleep(1)
driver.get(url)

def scrolltop(pos):
    js = "document.documentElement.scrollTop=%s" % pos
    driver.execute_script(js)
    

# 起始位置設為200，注意螢幕大小，我的螢幕為14吋。
pos = 200
for i in range(10):
    pos += 320
    scrolltop(pos)
    # 注意抓取的值為list，要一個一個取出。
    driver.find_elements_by_xpath("//div[@class='card-features']/a[@class='link-learn-more']")[i].click()
    time.sleep(1)
    driver.back()
    print("現在到第幾張卡:", i+1)
    scrolltop(pos)
    time.sleep(1)
