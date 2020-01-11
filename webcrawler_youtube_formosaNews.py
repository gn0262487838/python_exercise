from selenium.webdriver import Chrome
from pytube import YouTube
from pydub import AudioSegment
from Logger import Logger
import glob
import pandas as pd
import wave
import time
import os
import re

Logger = Logger(FILENAME="formosaNews")
'''

捲動chrome畫面

'''
def scrolltop(pos, driver):

    if not driver:
        return "pls build driver"

    if type(pos) != int:
        raise TypeError(f"{pos} must be number")

    js = f"document.documentElement.scrollTop={pos}"
    driver.execute_script(js)

def youtube_download(href):

    if type(href) != str:
        raise TypeError(f"{href} must be url")

    # 創建資料夾
    if not os.path.exists("./formosaNews"):
        os.makedirs("./formosaNews")

    yt = YouTube(href)
    # 標題去掉特殊符號並更改為_
    s = yt.title
    pattern = "\W"
    regex = re.compile(pattern)
    s = regex.sub("_", s)
    try:
        output_file = yt.streams.first().download("./formosaNews")
        # 在原存檔資料夾中重新命名檔名
        os.rename(output_file, f"./formosaNews/{s}.mp4")
        s = f"Download Success... {s}}"
        Logger.info(s)
    except:
        s = f"can't catch {href}"
        Logger.error(s)

def convert_audio_or_video_to_Audio(paths, ar=16000, ac=1, newFileName="wav"):
    # QUIZ 使用parameters調整聲道及取樣頻率，但無法轉檔成功
    params = {"-ar":ar,"-ac":ac}
    if type(paths) == list:
        Logger.info("Converting...")
        for i in paths:
            try:
                fileType = os.path.splitext(i)[1]
                if fileType == "." + newFileName:
                    s = f"filename extension is same : {fileType}"
                    Logger.error(s)
                    raise ValueError(s)

                unk_fileType = AudioSegment.from_file(i)
                unk_fileType = unk_fileType.set_channels(ac)
                unk_fileType = unk_fileType.set_frame_rate(ar)

                newName_Wav = os.path.split(i)[1].replace(f"{fileType}", "." + newFileName)
                unk_fileType.export(newName_Wav, format=newFileName, parameters=params)
                with wave.open(newName_Wav, "rb") as f:
                    s = "轉檔成功 : %s" % f.getparams()
                    Logger.info(s)
            except:
                s = f"Convert Error : {i}"
                Logger.error(s)
        Logger.info("===== Convert : Finish =====")

    elif type(paths) == str and os.path.exists(paths):
        Logger.info("Converting...")
        if fileType == "." + newFileName:
            s = f"filename extension is same : {fileType}"
            Logger.error(s)
            raise ValueError(s)
        fileType = os.path.splitext(i)[1]
        unk_fileType = AudioSegment.from_file(i)
        unk_fileType = unk_fileType.set_channels(ac)
        unk_fileType = unk_fileType.set_frame_rate(ar)
        newName_Wav = os.path.split(i)[1].replace(f"{fileType}", "." + newFileName)
        unk_fileType.export(newName_Wav, format=newFileName, parameters=params)
        with wave.open(newName_Wav, "rb") as f:
            s = f"轉檔成功 : {f.getparams()}"
            Logger.info(s)
        Logger.info("===== Convert : Finish =====")

def formosaNews_search_and_to_csv(url=None):
    if url == None:
        url = "https://www.youtube.com/user/FTVEnglishNews/videos"

    driver = Chrome()
    driver.maximize_window()
    time.sleep(2)
    driver.get(url)
    time.sleep(5)

    pos = 0
    hrefList = []
    titleList = []
    commentList = []
    idx = 0

    Logger.info("formosaNews downloading...")
    while True:
        a_ = driver.find_elements_by_xpath("//a[@id='video-title']")
        try:
            for i in a_:
                href = i.get_attribute("href")
                title = i.text
                if not title in titleList:
                    titleList.append(title)
                    if not href in hrefList:
                        hrefList.append(href)
        except:
            s = f"{href} is None or {title} is None or etc."
            Logger.error(s)

        pos += 200
        scrolltop(pos, driver)
        idx += 1
        if idx % 20 == 0:
            time.sleep(1)
            s = f"現在滾動第{idx}次"
            Logger.info(s)
            if idx % 200 == 0:
                Logger.info("===== title & href : Finish =====")
                break

    for i in hrefList:
        try:
            driver.get(i)
            driver.execute_script("document.body.style.zoom='0.8'")
            time.sleep(5)
            # 注意，YT有定義自己的標籤(非屬於html)
            comment = driver.find_element_by_css_selector("yt-formatted-string.content").text
            if comment == None:
                comment = "NULL"
            commentList.append(comment)
        except:
            s = f"Some Error on comment : {i}"
            Logger.error(s)
    Logger.info("===== comment : Finish =====")

    Logger.info("creating csv...")
    dic = {
        "title": titleList,
        "href": hrefList,
        "comment": commentList
    }
    df = pd.DataFrame(dic)
    df.to_csv("./formosaNews.csv", encoding="UTF-8", index=False)
    Logger.info("OK...")

if __name__=="__main__":

    df = pd.read_csv("./formosaNews.csv", encoding="UTF-8")
    hrefList = list(df["href"])

    Logger.info("YT downloading...")
    for url in hrefList:
        try:
            youtube_download(url)
        except:
            s = f"YT download Error : {url}"
            Logger.error(s)
    Logger.info("===== YT download : Finish =====")

    videoPathList = glob.glob("./formosaNews/*")
    convert_audio_or_video_to_Audio(videoPathList)
    Logger.info("=====    ALL FINISH    =====")
    Logger.Close()

'''
On 20191227
Error : url_encoded_fmt_stream_map
fix: pytube -> mixins.py 修正此函數最下面那段code

'''
# def apply_descrambler(stream_data, key):
#     """Apply various in-place transforms to YouTube's media stream data.

#     Creates a ``list`` of dictionaries by string splitting on commas, then
#     taking each list item, parsing it as a query string, converting it to a
#     ``dict`` and unquoting the value.

#     :param dict dct:
#         Dictionary containing query string encoded values.
#     :param str key:
#         Name of the key in dictionary.

#     **Example**:

#     >>> d = {'foo': 'bar=1&var=test,em=5&t=url%20encoded'}
#     >>> apply_descrambler(d, 'foo')
#     >>> print(d)
#     {'foo': [{'bar': '1', 'var': 'test'}, {'em': '5', 't': 'url encoded'}]}

#     """

#     # stream_data[key] = [
#     #     {k: unquote(v) for k, v in parse_qsl(i)}
#     #     for i in stream_data[key].split(',')
#     # ]
#     # logger.debug(
#     #     'applying descrambler\n%s',
#     #     pprint.pformat(stream_data[key], indent=2),
#     # )

#     if key == 'url_encoded_fmt_stream_map' and not stream_data.get('url_encoded_fmt_stream_map'):
#         formats = json.loads(stream_data['player_response'])[
#             'streamingData']['formats']
#         formats.extend(json.loads(stream_data['player_response'])[
#                        'streamingData']['adaptiveFormats'])
#         stream_data[key] = [{u'url': format_item[u'url'], u'type': format_item[u'mimeType'],
#                              u'quality': format_item[u'quality'], u'itag': format_item[u'itag']} for format_item in formats]
#     else:
#         stream_data[key] = [
#             {k: unquote(v) for k, v in parse_qsl(i)}
#             for i in stream_data[key].split(',')
#         ]
#     logger.debug(
#         'applying descrambler\n%s',
#         pprint.pformat(stream_data[key], indent=2),
#     )
