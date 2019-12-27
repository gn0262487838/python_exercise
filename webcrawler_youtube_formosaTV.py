from selenium.webdriver import Chrome
from pytube import YouTube
from pydub import AudioSegment
import glob
import pandas as pd
import wave
import time
import os

def scrolltop(pos):

    if not driver:
        return "pls build driver"
    
    if type(pos) != int:
        raise TypeError(f"{pos} must be number")

    js = f"document.documentElement.scrollTop={pos}" 
    driver.execute_script(js)


def youtube_download(href):

    if type(href) != str:
        raise TypeError(f"{href} must be url")

    # 轉檔後要儲存的資料夾
    if not os.path.exists("./formosaNews"):
        os.makedirs("./formosaNews")
    
    yt = YouTube(href)
    try:
        output_file = yt.streams.first().download("./formosaNews")
        print(f"Download Success... {yt.title}")
    except:
        print(f"Some Error : {href}")

def convert_audio_or_video_to_Audio(paths, ar=16000, ac=1, newFileName="wav"):
    params = {"-ar":ar,"-ac":ac}
    if type(paths) == list:
        for i in paths:
            try:
                fileType = os.path.splitext(i)[1]
                if fileType == "." + newFileName:
                    raise ValueError("file name is same.")
                unk_fileType = AudioSegment.from_file(i)
                unk_fileType = unk_fileType.set_channels(ac)
                unk_fileType = unk_fileType.set_frame_rate(ar)
                newName_Wav = os.path.split(i)[1].replace(f"{fileType}", "." + newFileName)
                unk_fileType.export(newName_Wav, format=newFileName, parameters=params)
                with wave.open(newName_Wav, "rb") as f:
                    print("轉檔成功 : ", f.getparams())
            except:
                with open("log.txt","a", encoding="UTF-8") as f:
                    f.write(f"Convert Error : {i}")
                print("Convert Error")
        print("All Finish...")

    if type(paths) == str and os.path.exists(paths):
        if fileType == "." + newFileName:
            raise ValueError("file name is same.")
        fileType = os.path.splitext(i)[1]
        unk_fileType = AudioSegment.from_file(i)
        unk_fileType = unk_fileType.set_channels(ac)
        unk_fileType = unk_fileType.set_frame_rate(ar)
        newName_Wav = os.path.split(i)[1].replace(f"{fileType}", "." + newFileName)
        unk_fileType.export(newName_Wav, format=newFileName, parameters=params)
        with wave.open(newName_Wav, "rb") as f:
            print("轉檔成功 : ", f.getparams())

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
            print(f"{href} is None or {title} is None or etc.")

        pos += 200
        scrolltop(pos)
        idx += 1
        if idx % 20 == 0:
            time.sleep(1)
            print(f"現在滾動第{idx}次")
            if idx % 200 == 0:
                print(f"滾動完畢...")
                break

    log = []
    for i in hrefList:
        try:
            driver.get(i)
            driver.execute_script("document.body.style.zoom='0.8'")
            time.sleep(5)
            comment = driver.find_element_by_css_selector("yt-formatted-string.content").text
            if comment == None:
                comment = "NULL"
            commentList.append(comment)
        except:
            print(f"Some Error on comment : {i}")
            log.append(i)

    print("===== comment download =====")

    print("creating csv...")
    dic = {
        "title": titleList,
        "href": hrefList,
        "comment": commentList
    }
    df = pd.DataFrame(dic)
    df.to_csv("./formosaNews.csv", encoding="UTF-8", index=False)
    print("Finish...")

    with open("log.txt", "a", encoding="UTF-8") as file:
        for i in log:
            file.write(i + "\n")
        print("log cover over...")

hrefDf = pd.read_csv("./formosaNews.csv", encoding="UTF-8")
hrefList = list(hrefDf)

for url in hrefList:
    try:
        youtube_download(url)
    except:
        with open("log.txt", "a", encoding="UTF-8") as f:
            f.write(f"YT download Error : {url}")
        print("YT download Error")
print("YT download Finish...")

print("strating convert...")
videoPathList = glob.glob("./formosaNews/*")
convert_audio_or_video_to_Audio(videoPathList)
print("Convert Finish...")


'''

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
