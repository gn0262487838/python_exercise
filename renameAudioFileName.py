# -*- coding:UTF-8 -*-
"""

寫一個轉換kenkone音檔檔名&紀錄時間csv。
記得把fileTimeStamp、worker.log連同scripts放在同一個資料夾內!!!

格式範例:
        fileTimeStamp:
        -rw-r--r-- 1 root root  466944 2020-02-12 08:50:23.936430331 +0000 e42feac2-8dff-441e-b6f6-cb9ef022de01.raw

        worker.log:
        2020-02-21 00:39:37 -    INFO:   decoder2: febb2967-34cc-4e19-b50b-04daf1546483: Got final result: evas_go


params:
        fileLog: 檔案排序後的文字檔
        audioFilePath: 音檔路徑
        testDay: YYYY-MM-DD
        newFileName: 命名新檔名

"""
import os
import sys
import pandas as pd
import glob
import re

fileLog = sys.argv[1]
audioFilePath = sys.argv[2]
testDay = sys.argv[3]
newFileName = sys.argv[4]


print("params====================================")
print(fileLog, audioFilePath, testDay, newFileName)
print("==========================================")

cwd = os.getcwd()
contentArray = []

with open(fileLog, "r", encoding="UTF-8") as f:
    content = f.readlines()

with open("./worker.log", "r", encoding="UTF-8") as f:
    workercontent = f.readlines()

searchworkercontent = []
patternTime = str(testDay)
regex_time = re.compile(patternTime)
for i in workercontent:
    i.replace("\n", "")
    if regex_time.search(i):
        searchworkercontent.append(i)

order = 1
df = pd.DataFrame(columns=["Time", "OriginFileName",
                           "NewFileName", "voiceContent", "Recognize"])
print("==========================================")
print("START CONVERT")
print("==========================================")
for line in content:
    try:
        newFileName_ = newFileName + str(order)
        lineArray = line.replace("\n", "").strip().split(" ")
        fileName = lineArray[-1].split(".")[0]
        fileCreateTime = lineArray[-3].split(".")[0]
        testFileDay = lineArray[-4]
        if testFileDay == testDay:
            pattern = fileName + ": Got final result"
            regex = re.compile(pattern)
            for string in searchworkercontent:
                if regex.search(string):
                    recog = string.split(" ")[-1]
                    break
                else:
                    recog = ""

            os.rename(cwd + "\\" + audioFilePath + "\\" + fileName + ".raw",
                      cwd + "\\" + audioFilePath + "\\" + newFileName_ + ".raw")
            order = order + 1
            s = pd.Series([fileCreateTime, fileName,
                           newFileName_, "", recog], index=["Time", "OriginFileName", "NewFileName", "voiceContent", "Recognize"])
            df = df.append(s, ignore_index=True)
    except IndexError:
        print("==========================================")
        print("CONVERT FINISH")
        print("==========================================")

print("==========================================")
print("SAVE")
with open(newFileName + ".csv", "w", encoding="UTF-8") as f:
    df.to_csv(f, index=False)
print("SAVED")
print("==========================================")


if __name__ == "__main__":
    pass
