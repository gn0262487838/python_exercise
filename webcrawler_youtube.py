from selenium.webdriver import Chrome
from pytube import YouTube
from pydub import AudioSegment
import pandas as pd
import wave
import time
import os

def scrolltop(pos : int):

    if type(pos) != int:
        raise TypeError(f"{pos} must be number")
    
    js = "document.documentElement.scrolltop = %s" % pos
    driver.execute_script(js)

def youtube_download(url : str, path : str, reName : str):
    
    if type(url) != str:
        raise TypeError(f"{url} must be url")
    
    # 轉檔後要儲存的資料夾
    if not os.path.exists(path):
        os.makedirs(path)

    yt = YouTube(url)
    try:
        output_file = yt.streams.filter(progressive=True, file_extension="mp4").download(path)
        os.rename(output_file, reName)
    except:
        print(f"Some Error : {url}")

def convert_audio_or_video_to_Audio(paths, ar=16000, ac=1, newFileName="wav"):
    params = ["-vn ","-ar",ar,"-ac",ac]
    if type(paths) == list: 
        for i in paths:
            fileType = os.path.splitext(i)[1]
            if fileType == "." + newFileName:
                raise ValueError("file name is same.")
            unk_fileType = AudioSegment.from_file(i)
            newName_Wav = os.path.split(i)[1].replace(f"{fileType}", "." + newFileName)
            unk_fileType.export(newName_Wav, format=newFileName, parameters=params)    
            with wave.open(newName_Wav, "rb") as f:
                print("轉檔成功 : ",f.getparams())
            
    if type(paths) == str and os.path.exists(paths):
        if fileType == "." + newFileName:
            raise ValueError("file name is same.")
        fileType = os.path.splitext(i)[1]
        unk_fileType = AudioSegment.from_file(i)
        newName_Wav = os.path.split(i)[1].replace(f"{fileType}", "." + newFileName)
        unk_fileType.export(newName_Wav, format=newFileName, parameters=params)    
        with wave.open(newName_Wav, "rb") as f:
            print("轉檔成功 : ",f.getparams())
                
url = "https://www.youtube.com/user/FTVEnglishNews/videos"

driver = Chrome()
driver.maximize_window()
time.sleep(2)
driver.get(url)
time.sleep(3)

pos = 0
hrefList = []
titleList = []
commentList = []
idx = 0
while True:
    a_ = driver.find_elements_by_xpath("//a[@id='video-title']")
    try:
        for i in a_:
            href = i.get_attribute("href")
            title = i.text
            if title != None and title not in titleList:
                titleList.append()
                if href != Nnoe and href not in hrefList:
                    hrefList.append(href)
    except:
        print(f"{href} is None or {title} is None or etc.")

    pos += 200
    scrolltop(pos)
    idx += 1
    if idx % 50 == 0:
        time.sleep(1)
    if idx % 300 == 0:
        break

for i in hrefList:
    driver.get(i)
    time.sleep(1)
    comment = driver.find_element_by_css_selector("yt-formatted-string.content").text
    commentList.append(comment)

dic = {
    "title":titleList,
    "href":hrefList,
    "comment":commentList
}
df = pd.dataFrame(dic)
df.to_csv("./formosaNews.csv", encoding="UTF-8")

