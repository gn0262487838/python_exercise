# -*- coding=UTF-8 -*- #

'''

kit

'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

'''

設計一個可以爬蟲 ptt creditcard 推文

'''

page = 3155
pttdf = pd.DataFrame(columns=["url","title","content","pos","neg"])
print("=" * 50 + "Start Loading" + "=" * 50)
while page > 3000:

    print("現在第{}頁:".format(page))
    Url = "https://www.ptt.cc/bbs/creditcard/index"+ str(page) +".html"
    
    response = requests.get(Url)
    response.encoding = "UTF-8"
    html = BeautifulSoup(response.text, "html.parser")

    title_html = html.find_all("div", {"class":"title"})
    domainName = "https://www.ptt.cc"

    for i in title_html:
        # 標題攝取
        title = i.text.replace("\n","")
        # 判定有無null
        if "本文已被刪除" in title or "公告" in title:
            continue
        # 網址攝取並寫入pf
        url = domainName + i.find("a").attrs["href"]

        # 載入子網頁
        response = requests.get(url)
        url_html = BeautifulSoup(response.text, "html.parser")
        main_content = url_html.find("div", {"id":"main-content"})

        try:
            # 移除不要的元素
            main_content.find("div", {"class": "article-metaline-right"}).extract()
            for j in main_content.find_all("div",{"class":"article-metaline"}):
                j.extract()
            for j in main_content.find_all("span",{"class":"f2"}):
                j.extract()
        except AttributeError:
            print("好像有問題喔，等等再看看:{}".format(title))

        # 拿取正反面推文
        posBag = ""
        negBag = ""

        main_content_push = main_content.find_all("div", class_="push")
        for k in main_content_push:
            if "噓" in k.find_all("span")[0].text:
                neg = k.find_all("span")[2].text
                negBag = negBag + neg + "\n"
            else:
                pos = k.find_all("span")[2].text
                posBag = posBag + pos + "\n"

        for j in main_content.find_all("div", class_="push"):
            j.extract()

        # 把東西一一寫入pd
        content = main_content.text.replace(" ","").replace("-","").replace("SentfromJPTTonmyAsusASUS_Z01RD.","")
        s = pd.Series([url, title, content, posBag, negBag], index=["url", "title", "content", "pos", "neg"])
        pttdf = pttdf.append(s, ignore_index=True)
    page -= 1

print("="*50 + "好像結束摟" + "="*50)
print("="*50 + "開始儲存中" + "="*50)
pttdf.to_csv("ptt_content.csv",encoding="UTF-8", index=False)
print("="*50 + "儲存完畢" + "="*50)
