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

def scrolldown():
    js = "document.documentElement.scrollTop=10000"
    driver.execute_script(js)

def backpage(page):
    driver.find_element_by_id(
        "layout_0_rightcontent_0_updatepanel_1_RptPagination_HlkPageNumber_{}".format(page)).click()


# 起始位置設為200，注意螢幕大小，我的螢幕為14吋。
page = 1
while page < 5:
    pos = 200
    for i in range(10):
        pos += 320
        scrolltop(pos)
        # 注意抓取的值為list，要一個一個取出。
        driver.find_elements_by_xpath("//div[@class='card-features']/a[@class='link-learn-more']")[i].click()
        time.sleep(1)
        if page == 1:
            driver.back()
            print("現在到第幾頁:", page, "到第幾張卡片:", i + 1)
            scrolltop(pos)
            time.sleep(1)
        else:
            driver.back()
            scrolldown()
            backpage(page)
    backpage(page)
    time.sleep(1)
    page += 1
print("好像沒東西喔!!!")
