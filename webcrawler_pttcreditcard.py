import requests
from bs4 import BeautifulSoup
import pandas as pd

Url = "https://www.ptt.cc/bbs/creditcard/index.html"

pttdf = pd.DataFrame(columns=["url","title","content","pos","neg"])

response = requests.get(Url)
response.encoding = "UTF-8"
html = BeautifulSoup(response.text, "html.parser")

title_list = html.find_all("div", {"class":"title"})

ptt_url = "https://www.ptt.cc"
titles = []
hrefs = []
for i in title_list:
    if i.find("a"):
        title = i.text.replace("\n","")
        s = pd.Series([title],index=["title"])
        pttdf = pttdf.append(s, ignore_index=True)

        href = i.find("a").attrs["href"]
        href = ptt_url + href
        s = pd.Series([href],index=["url"])
        pttdf = pttdf.append(s,ignore_index=True)
        hrefs.append(href)

for i in hrefs:
    url = i
    response = requests.get(url)
    response.encoding = "UTF-8"
    html = BeautifulSoup(response.text, "html.parser")
    content = html.find("div",{"id":"main-content"})

    for j in content.find_all("div",{"class":"article-metaline"}):
        j.extract()
    content.find("div",{"class":"article-metaline-right"}).extract()
    for j in content.find_all("span",{"class":"f2"}):
        j.extract()

    if content.find_all("div",class_="push"):
        posBox = ''
        negBox = ''
        print(content.find_all("div",class_="push")[1])
        for j in content.find_all("div",class_="push")[1]:
            print(j)
            if "噓" in j.find("span",class_="push-tag"):
                jstr = j.find("span", class_="push-content").text
                negBox = negBox + jstr + "\n"
            else:
                jstr = j.find("span", class_="push-content").text
                posBox = posBox + jstr + "\n"
            j.extract()
        s = pd.Series([posBox, negBox], index=["pos","neg"])
        pttdf = pttdf.append(s, ignore_index=True)

    s = pd.Series(content.text.replace(" ","").replace("-","").replace("SentfromJPTTonmyAsusASUS_Z01RD.",""),index=["content"])
    pttdf = pttdf.append(s, ignore_index=True)

print(pttdf)
