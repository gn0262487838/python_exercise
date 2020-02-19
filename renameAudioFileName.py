# -*- coding:UTF-8 -*-
"""

寫一個轉換kenkone音檔檔名&紀錄時間csv

格式範例:
        -rw-r--r-- 1 root root  466944 2020-02-12 08:50:23.936430331 +0000 e42feac2-8dff-441e-b6f6-cb9ef022de01.raw

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

fileLog = sys.argv[1]
audioFilePath = sys.argv[2]
testDay = sys.argv[3]
newFileName = sys.argv[4]


print("params====================================")
print(fileLog, audioFilePath, testDay, newFileName)
print("==========================================")

cwd = os.getcwd()
contentArray = []

with open(fileLog) as f:
    content = f.readlines()

order = 1
df = pd.DataFrame(["Time", "OriginFileName", "NewFileName",
                   "voiceContent", "recognize"])
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
            os.rename(cwd + "\\" + audioFilePath + "\\" + fileName + ".raw",
                      cwd + "\\" + audioFilePath + "\\" + newFileName_ + ".raw")
            order = order + 1
            s = pd.Series([fileCreateTime, fileName, newFileName_,
                           "", ""])
            df = df.append(s, ignore_index=True)
    except IndexError:
        print("==========================================")
        print("CONVERT FINISH")
        print("==========================================")

print("==========================================")
print("SAVE")
df.to_csv(newFileName + ".csv", index=False)
print("SAVED")
print("==========================================")


if __name__ == "__main__":
    pass
