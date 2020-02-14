#coding:utf-8
'''
@Time: 2020/2/13 12:33
@author: Tokyo
@file: code_03_PackingMachine.py
@desc:
有n个打包机器从左到右一字排开，上方有一个自动装置会抓取一批放物品到每个打
包机上，放到每个机器上的这些物品数量有多有少，由于物品数量不相同，需要工人
将每个机器上的物品进行移动从而到达物品数量相等才能打包。每个物品重量太大、
每次只能搬一个物品进行移动，为了省力，只在相邻的机器上移动。请计算在搬动最
小轮数的前提下，使每个机器上的物品数量相等。如果不能使每个机器上的物品相同，
返回-1。
例如[1,0,5]表示有3个机器，每个机器上分别有1、0、5个物品，经过这些轮后：
第一轮：1 0 <- 5 => 1 1 4 第二轮：1 <-1<- 4 => 2 1 3 第三轮：
2 1 <- 3 => 2 2 2
移动了3轮，每个机器上的物品相等，所以返回3
例如[2,2,3]表示有3个机器，每个机器上分别有2、2、3个物品，
这些物品不管怎么移动，都不能使三个机器上物品数量相等，返回-1
'''

def packingMachine(arr):
    if arr is None or arr == []:
        return -1
    if sum(arr)%len(arr) != 0:
        return -1

    avg = sum(arr) / len(arr)
    leftRest = 0
    res = 0
    for i in range(len(arr)):
        left = leftRest - i * avg
        right = sum(arr[i+1:]) - (len(arr)-i-1)*avg
        if left < 0 and right < 0:
            res = max(res, abs(left+right))
        else:
            res = max(res, abs(left), abs(right))
        leftRest += arr[i]

    return res

if __name__ == '__main__':
    arr = [100,20,0,0]
    print(packingMachine(arr))