# -*- coding:utf-8 -*-

'''
使用前小手冊:

for windows
1. 請先下載ffmpeg
2. 設定系統環境變數
                  1. 本機(or 我的電腦)點選右鍵>內容>進階管理設定>進階>環境變數>系統環境變數>新增
                  2. 變數名稱:FFMPEG_HOME
                     變數值:ffmpeg的路徑 C:\Users\xxx\yyy\ffmpeg\bin
                     ok按確認
                  3. 再找到path，按下編輯>新增>貼上%FFMPEG_HOME%
                  4. 最後再按3次確認
                  5. 重新開機
3. pip install pydub
'''

import os
import wave
from pydub import AudioSegment

'''
設計一個aac轉wav
input : .aac
output : 
        1. .wav 
        
        以下尚未完成，coming soon
        2. channel = 1
        3. framerate = 16000 
'''
def convert_aac_to_wav(aacPath):
    # 還在思考路徑怎麼寫...

    # convert aac to wav
    aac = AudioSegment.from_file(aacPath)
    aac.export(aacPath.split(".")[-2].replace("/","") + ".wav", format="wav")

    # check data
    voice = wave.open(aacPath.split(".")[-2].replace("/","") + ".wav", "rb")
    channel, _, framerate, _, _, _ = voice.getparams()
    print(f"###開始轉檔###\n聲道數:{channel} 音頻:{framerate}\n###轉檔成功###")
