from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time

url = "https://www.cathaybk.com.tw/cathaybk/personal/credit-card/cards/intro/list/"

'''測試

# 設定無介面視窗
driveroptions = Options()
driveroptions.add_argument("--headless")

'''

# 開啟並取得國泰信用卡網頁。
driver = Chrome("./chromedriver.exe", chrome_options=driveroptions)
# 注意是否要放大，或自訂螢幕大小。
driver.maximize_window()
time.sleep(1)
driver.get(url)

'''測試

# 頁面縮放，但縮放完程式就暫停了...
# driver.execute_script("document.body.style.zoom='0.8'")

'''


def scrolltop(pos):
    js = "document.documentElement.scrollTop=%s" % pos
    driver.execute_script(js)

def scrolldown():
    js = "document.documentElement.scrollTop=10000"
    driver.execute_script(js)

def backpage(page):
    driver.find_element_by_id(
        "layout_0_rightcontent_0_updatepanel_1_RptPagination_HlkPageNumber_{}".format(page-1)).click()
    # 給他一秒鐘的時間跑
    time.sleep(1)

# 起始位置設為200，注意螢幕大小，我的螢幕為14吋。
page = 1
while page < 5:
    pos = 200
    for i in range(10):
        print("現在到第幾頁:", page, "到第幾張卡片:", i + 1)
        pos += 320
        scrolltop(pos)
        # 注意抓取的值為list，要一個一個取出。
        driver.find_elements_by_xpath("//div[@class='card-features']/a[@class='link-learn-more']")[i].click()
        time.sleep(1)
        if page == 1:
            driver.back()
        else:
            driver.back()
            scrolldown()
            backpage(page)
    page += 1
    backpage(page)
print("好像沒東西喔!!!")
