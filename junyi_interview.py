# /usr/bin/python3.7
# -*- coding:utf-8 -*-
# Author: HU REN BAO
# History:
#         1. 20200413 first commit
# Contact:
#         Email:gn0262487838@gmail.com
#

'''

task 1

'''


def convert_str(s):
    '''

    params:
            s: str

    goal:
        covert "abc abc" into "cba cba"

    '''
    if type(s) is not str:
        raise TypeError(f"{s} must be str")

    newStr = s[::-1]
    result = f'''
        Task One-one
        Input: {s}
        Output:{newStr}
    '''
    print(result)

    return result


def convert_word(s):
    '''

    params:
            s: str

    goal:
        covert "abc ddffg" into "cba gffdd"

    '''

    if type(s) is not str:
        raise TypeError(f"{s} must be str")

    split_box = s.split(" ")
    join_box = []
    for word in split_box:
        word = word[::-1]
        join_box.append(word)

    newStr = " ".join(join_box)
    result = f'''
        Task One-two
        Input: {s}
        Output:{newStr}
    '''
    print(result)

    return result


'''

task 2

'''


def filter_(number):
    '''
    becuase only use build in python function, so i decide to ignore float type.

    params:
            number: int

    goal:
        1. show 1 to number and calculate number of elements
        ex. if number = 10,then show 1,2,4,7,8 and number of elements is equal to 5

    '''

    if type(number) is str:
        number = int(number)
    elif type(number) is float:
        raise TypeError(f"{number} must be int")

    num_box = []
    for i in range(1, number+1, 1):
        num_box.append(i)

    remove_box = []
    for j in num_box:
        if j % 3 == 0 and j % 5 != 0:
            remove_box.append(j)
        elif j % 3 != 0 and j % 5 == 0:
            remove_box.append(j)

    for k in remove_box:
        num_box.remove(k)

    lenNum = len(num_box)
    result = f'''
        Task Two
        Input:  {number}
        num_box:{num_box}
        Output: {lenNum}
    '''
    print(result)

    return result


'''

task 3

Ans:
    因為標籤都貼錯，所以說明
    標籤鉛筆  裡面只可能會裝 原子筆 或 混合
    標籤原子筆裡面只可能會裝 鉛筆   或 混合
    標籤混合  裡面只可能會裝 原子筆 或 鉛筆

    假設一:
        拿標籤鉛筆一袋，
                    標籤鉛筆  標籤混合  標籤原子筆
        狀況一:裡面裝 原子筆 >  鉛筆   >   混合
                    標籤鉛筆 標籤原子筆 標籤混合
        狀況二:裡面裝 混合   >  鉛筆   >   混合

    假設二:
        拿標籤原子筆一袋，
                    標籤原子筆 標籤混合 標籤鉛筆
        狀況一:裡面裝 鉛筆   >  原子筆  > 混合
                    標籤原子筆 標籤鉛筆  標籤混合
        狀況二:裡面裝 混合   >  原子筆  > 鉛筆

    假設三:
        拿標籤混合一袋，
                    標籤混合  標籤鉛筆  標籤原子筆
        狀況一:裡面裝 原子筆 >  混合  >   鉛筆
                    標籤混合  標籤原子筆 標籤鉛筆
        狀況二:裡面裝 鉛筆   >  混合  >  原子筆

'''


'''

task 4

ans:
    第一句300 - 30 = 270(三人各出的金額)
    第二句270 X 3 = 810(三人合計出的錢)明顯就出了問題，
    原因服務生退給他們每人30元(共九十元)，實際上總額度是810 + 90 才正確。
    況且服務生私藏60的金額也包含在他們每人出270的金額裡面，這60元也要他們三人均分(實際上三人都不知道他們每人又多出了20元)，故後面邏輯也就都錯誤。
    實際上的算法是
    300 - 30 - 20 = 250(三人實際上每人應該出的金額)
    250 X 3 = 750
    750 + 60 + (30 X 3) = 900

'''

if __name__ == "__main__":

    str_ = input("please key a sentence:\n")
    if str_ == None or str_ == "":
        str_ = "abcd efgh"

    word_ = input("please key more two word:\n")
    if word_ == None or word_ == "":
        word_ = "hello world"

    num_ = input("please key a number:\n")
    if num_ == None or num_ == "":
        num_ = 15

    dict_ = {
        "str_": str_,
        "word_": word_,
        "num_": num_
    }

    convert_str(dict_["str_"])
    convert_word(dict_["word_"])

    filter_(dict_["num_"])
