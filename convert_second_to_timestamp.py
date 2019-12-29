# -*- coding:UTF-8 -*-
'''

only for audacity use
使用標籤剪輯音檔時，再匯出多個音檔檔案後再匯出標籤軌道資訊，
因裡面的時間是總秒數，故寫一個換算成分鐘:秒數:毫秒

'''
import pandas as pd
import re

FILENAME = "20191224_voiceRecord"

with open("./標籤軌道.txt","r",encoding="UTF-8") as f:
    content = f.readlines()

startList = []
endList = []
numList = []
for i in content:
    line = i.split()
    regex = re.compile(r"(\d+)(.)(\d{3})")
    num_0 = regex.search(line[0])
    start_s = int(num_0.group(1))
    start_q, start_r, start_ms = start_s // 60, start_s % 60, num_0.group(3)
    startTime = f"{start_q:2d}:{start_r:2d}:{start_ms}"

    num_1 = regex.search(line[1])
    end_s = int(num_1.group(1))
    end_q, end_r, end_ms = end_s // 60, end_s % 60, num_1.group(3)
    endTime = f"{end_q:2d}:{end_r:2d}:{end_ms}"

    num = line[2]
    startList.append(startTime)
    endList.append(endTime)
    numList.append(num)

dic = {
    "STARTTIME":startList,
    "ENDTIME":endList,
    "NAME":numList
}
df = pd.DataFrame(dic)
df.to_csv(FILENAME, index=False, encoding="UTF-8")
