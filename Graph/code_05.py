#coding:utf-8
'''
@Time: 2020/3/26 20:07
@author: Tokyo
@file: code_05.py
@desc:
'''

def taowa(arr,k,n):
    if arr is None or arr == []:
        return 0
    dp = [0]+arr
    for i in range(1,k+1):
        for j in range(1,n+1):
            dp[j] = dp[j]+dp[j-1]
    return dp[n]

if __name__ == '__main__':
    arr = [1,0,0,0]
    print(taowa(arr,3,4))
