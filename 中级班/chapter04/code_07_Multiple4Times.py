#coding:utf-8
'''
@Time: 2020/2/17 15:11
@author: Tokyo
@file: code_07_Multiple4Times.py
@desc:
给定一个数组arr，如果通过调整可以做到arr中任意两个相邻的数字相乘是4的倍数，
返回true；如果不能返回false
'''

def multiple4(arr):
    if arr is None or arr == []:
        return False
    odd, fourtimes, notfour = 0, 0, 0
    for i in arr:
        if i %2 != 0:
            odd += 1
        else:
            if i % 4 == 0:
                fourtimes += 1
            else:
                notfour += 1
    # 只有奇数和4的倍数
    if notfour == 0:
        if odd == 1:
            return True if fourtimes>=1 else False
        else:
            return True if fourtimes>= odd-1 else False
    else:
        return True if fourtimes >= odd else False

if __name__ == '__main__':
    arr = [2,2,3,2,4]
    print(multiple4(arr))
