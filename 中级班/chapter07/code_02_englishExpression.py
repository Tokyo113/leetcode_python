#coding:utf-8
'''
@Time: 2020/2/24 18:24
@author: Tokyo
@file: code_02_englishExpression.py
@desc:
同上题，将n转化为英文表达
按照个十百千，million,billion
'''

def convertEnglish(n):
    pass

def num1to19(n):
    if n<1 or n>19:
        return ''
    arr = ['one', 'two', 'three', 'four', 'five', 'six',
           'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
           'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
           'eighteen', 'nineteen']
    return arr[n-1]

def num1to99(n):
    if n<1 or n>99:
        return ''
    if n<=19:
        return num1to19(n)
    shi = n//10
    arr = ["Twenty ", "Thirty ", "Forty ", "Fifty ","Sixty ",
           "Seventy ", "Eighty ", "Ninety "]
    if n%10 == 0:
        return arr[shi-2]
    else:
        return arr[shi-2]+num1to19(n%10)


def num1to999(n):
    if n<1 or n>999:
        return ''
    if n<=99:
        return num1to99(n)
    bai = n//100
    if n%100 == 0:
        return num1to19(bai)+' hundred '
    return num1to19(bai)+' hundred '+'and '+num1to99(n%100)

def num1to999999(n):
    if n<1 or n>999999:
        return ''
    if n<=999:
        return num1to999(n)
    qian = n//1000
    if n%1000 ==0:
        return num1to999(qian)+'thousand'
    return num1to999(qian)+' thousand '+'and '+ num1to999(n%1000)


def num1to999999999(n):
    if n<1 or n>999999999:
        return ''
    if n<999999:
        return num1to999999(n)
    baiwan = n//1000000
    if n%1000000 ==0:
        return num1to999(baiwan)+' million'
    else:
        return num1to999(baiwan)+' million '+num1to999999(n%1000000)
if __name__ == '__main__':
    print(num1to999999999(999999999))