'''

def train photo download fun.

'''

import requests
from bs4 import BeautifulSoup
import os

def picture_download(keyword, maxpage, file):

    imgbox = []
    page = 1
    print("start downloading")
    while page <= int(maxpage):
        url = "https://pixabay.com/zh/images/search/"+ keyword +"/?pagi="+ str(page)

        header = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
        response = requests.get(url, headers = header)
        response.encoding="utf-8"
        html = BeautifulSoup(response.text, "html.parser")

        imglist = html.find_all("div", class_="item")

        print("="*15 + "downloading" + str(page) + "="*15)
        for i, j in enumerate(imglist):
            if j.find("img")["src"] in imgbox:
                print("samepicture")
                continue
            else:
                if j.find("img")["src"] == "/static/img/blank.gif":
                    img = j.find("img")["data-lazy"]
                    imgbox.append(img)
                elif j.find("img")["src"] != "/static/img/blank.gif":
                    img = j.find("img")["src"]
                    imgbox.append(img)
                else:
                    print("noting")
                    continue

            filename = "./"+ file +"/"
            filename_img = filename + keyword + "_" + str(page)+"_"+ str(i) + ".jpg"

            if not os.path.exists(filename):
                os.mkdir(filename)

            response_img = requests.get(img, headers = header)
            try:
                with open(filename_img, "wb")as f:
                    f.write(response_img.content)
            except:
                print("something Error")

        page += 1

    print("done...")

keyword = input("keyword:")
maxpage = input("maxpage:")
file = input("filename:")

picture_download(keyword, maxpage, file)
