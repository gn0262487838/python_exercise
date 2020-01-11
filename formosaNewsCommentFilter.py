# -*- coding:UTF-8 -*-
# python version : 3.7.4

'''

寫一個可以初步篩選內容符號篩選器並儲存為.csv

'''

import re
import pandas as pd

df = pd.read_csv("formosaNews.csv", encoding="UTF-8")

def Filter_NT(matched):
    s = matched.group("value")
    s = s.replace("NT$", "")
    s = s + " NT"
    return s


def Filter_PERCENT(matched):
    s = matched.group()
    s = s.replace(".", " point ")
    s = s.replace("%", " percent")
    return s


def tran(s):
    s = re.sub(",", "", s)
    s = re.sub('"', "", s)
    s = re.sub("''", "'", s)
    s = re.sub("“", "", s)
    s = re.sub("”", "", s)
    s = re.sub("’", "'", s)
    s = re.sub("", "", s)
    s = re.sub("\?", " ", s)
    s = re.sub("–", "", s)
    s = re.sub("--", " ", s)
    s = re.sub(" - ", " ", s)
    s = re.sub("…", "", s)

    # 注意re.sub(pattern, str or func, 等著被替代的字串)
    s = re.sub("(?P<value>NT\$\s?\d*)", Filter_NT, s)
    s = re.sub("(\d+.\d*%)", Filter_PERCENT, s)

    s = re.sub("\.", " ", s)

    return s


df["comment"] = df["comment"].apply(tran)
df.to_csv("./formosaNewsComment.csv", index=False)
