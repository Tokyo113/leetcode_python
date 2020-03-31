#coding:utf-8
'''
@Time: 2020/3/26 19:18
@author: Tokyo
@file: code02.py
@desc:
'''

def round1(arr):
    if arr is None or arr == []:
        return 0

    pi = 3.1415926535
    if len(arr) == 1:
        return round(pi*arr[0]*arr[0],5)
    if len(arr)%2 != 0:
        a = round(pi*arr[0]*arr[0],5)
        i = 2
        while i < len(arr):
            a += pi*(arr[i]**2)-pi*(arr[i-1]**2)
            i += 2
        return round(a,5)
    else:
        i = 1
        a = 0
        while i < len(arr):
            a += pi*(arr[i]**2)-pi*(arr[i-1]**2)
            i += 2
        return round(a,5)


if __name__ == '__main__':
    arr = [1,2]
    print(round1(arr))
