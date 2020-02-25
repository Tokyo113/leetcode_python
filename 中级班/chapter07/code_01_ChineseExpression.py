#coding:utf-8
'''
@Time: 2020/2/24 17:11
@author: Tokyo
@file: code_01_ChineseExpression.py
@desc:
把一个数字用中文表示出来。数字范围为 [0, 99999]。
为了方便输出，使用字母替换相应的中文，万W 千Q 百B 十S 零L。使用数字取代中
文数字注：对于 11 应该表示为 一十一(1S1)，而不是十一(S1)
输入描述：
数字 0（包含）到 99999（包含）。
输出描述：
用字母替换相应的中文，万W 千Q 百B 十S 零L
示例1:
输入
12001
输出
1W2QL1

思路：
按个十百千分别定制，
注意特殊情况
1000一千， 1001一千零一，1012一千零一十二，12十二
'''

def convertChinese(n):
    if n == 0:
        return '零'
    res = ''
    if n<0:
        res = '负'
    n = abs(n)


    if n<= 99999999:
        return res+num1to99999999(n)
    yi = n//100000000
    qianwan = (n%100000000)//10000000
    if n%100000000 == 0:
        return res+num1to99999999(yi)+'亿'
    if qianwan == 0:
        return res+num1to99999999(yi)+'亿'+'零'+num1to99999999(n%100000000)
    else:
        return res+num1to99999999(yi) + '亿' + num1to99999999(n % 100000000)






def num1to9(n):
    if n<1 or n>9:
        return ''
    arr = ['一','二', '三', '四', '五', '六', '七', '八', '九']
    return arr[n-1]

def num1to99(n):
    if n<1 or n>99:
        return ''
    if n<=9:
        return num1to9(n)
    shi = n//10
    if shi == 1:
        return '十'+num1to9(n%10)
    else:
        return num1to9(shi)+'十'+num1to9(n%10)



def num1to999(n):
    if n<1 or n>999:
        return ''
    if n<=99:
        return num1to99(n)
    bai = n//100
    shi = (n%100)//10
    if n%100 == 0:
        return num1to9(bai)+'百'
    if shi == 1:
        return num1to9(bai)+'百一'+num1to99(n%100)
    elif shi == 0:
        return num1to9(bai)+'百'+'零'+num1to9(n%10)
    else:
        return num1to9(bai)+'百'+num1to99(n%100)


def num1to9999(n):
    if n<1 or n>9999:
        return ''
    if n<=999:
        return num1to999(n)
    qian = n//1000
    bai = (n%1000)//100
    if n%1000 == 0:
        return num1to9(qian)+'千'
    if bai == 0:
        return num1to9(qian)+'千'+'零'+num1to99(n%100)
    else:
        return num1to9(qian)+'千'+num1to999(n%1000)

def num1to99999999(n):
    if n<1 or n>99999999:
        return ''
    if n<=9999:
        return num1to9999(n)
    wan = n//10000
    qian = n%10000
    if n%10000 == 0:
        return num1to9999(wan)+'万'
    if qian < 1000:
        return num1to9999(wan)+'万'+'零'+num1to9999(qian)
    else:
        return num1to9999(wan) + '万' + num1to9999(qian)



if __name__ == '__main__':
    print(convertChinese(-101100001))