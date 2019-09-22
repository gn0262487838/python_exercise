# -*- UTF-8 -*- #
'''

import kit

'''
from urllib.request import urlretrieve
from selenium.webdriver import Chrome
import time
import os

'''

Main

'''
class Crawler():

    def __init__(self):
        self.url = url
        self.xpath = xpath

    def Driver(self, url):
        driver = Chrome("./chromedriver")
        driver.maximize_window()
        time.sleep(1)
        driver.get(url)
        return driver

    def download_pic(self, driver, keyword):
        imgurlbox = []
        pos = 0
        l = 1
        print("start downloading")
        for i in range(50):
            print("{} scroll {} times".format("="*15,i))
            pos += 500
            js = "document.documentElement.scrollTop=%s" % pos
            driver.execute_script(js)
            time.sleep(3)
            for j, k in enumerate(driver.find_elements_by_xpath(xpath)):
                try:
                    imgurl = k.get_attribute("src")
                    filename = "./{}/".format(keyword)
                    file = filename + "{}_{}.jpg".format(l, j)
                    if not imgurl in imgurlbox:
                        if not os.path.exists(filename):
                            os.mkdir(filename)
                        urlretrieve(imgurl, file)
                    else:
                        print("samepicture")
                        continue
                    imgurlbox.append(imgurl)
                except OSError:
                    print("OSError")
                    print(pos)
                    break
            l += 1
        print("done...")

if __name__ =="__main__":
    '''
    
    設定要抓取圖片的網站，並定位圖片位置，最後設定存檔資料夾名稱。
    
    '''
    url = "https://pic.sogou.com/pics?query=%8E%9B%B8%E7&di=2&_asf=pic.sogou.com&w=05009900"
    # 最前面要雙斜線
    xpath = '//div[@id="imgid"]/ul/li/a/img'
    keyword = input("請輸入您要的資料夾名稱：")

    '''
    
    main.py
    
    '''
    craw = Crawler()
    driver = craw.Driver(url)
    craw.download_pic(driver, keyword)
    driver.close()
