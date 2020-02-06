#coding:utf-8
'''
@Time: 2019/12/10 21:59
@author: Tokyo
@file: code_11_HorseJump.py
@desc:
象棋中马的跳法
【题目】
请同学们自行搜索或者想象一个象棋的棋盘，然后把整个棋盘放入第一象限，棋盘的最左下
角是(0,0)位置。那么整个棋盘就是横坐标上9条线、纵坐标上10条线的一个区域。给你三个
参数，x，y，k，返回如果“马”从(0,0)位置出发，必须走k步，最后落在(x,y)上的方法数
有多少种？
'''



def horseDP(x,y,k):
    dp = [[[0 for i in range(k+1)]for i in range(10)]for i in range(9)]

    for z in range(k + 1):
        for row in range(9):
            for col in range(10):

                if z == 0:
                    dp[row][col][z] = 1 if row==0 and col == 0 else 0
                else:
                    dp[row][col][z] = findValue(dp,row+2, col+1, z-1)+findValue(dp,row-2, col+1,z-1)+\
                    findValue(dp,row+1,col+2,z-1)+findValue(dp,row-1,col+2,z-1)+\
                    findValue(dp,row+2,col-1,z-1)+findValue(dp,row-2,col-1,z-1)+\
                    findValue(dp,row+1,col-2, z-1)+findValue(dp,row-1,col-2,z-1)

    return dp[x][y][k]



def findValue(dp,row,col,z):
    if row < 0 or row >8 or col < 0 or col >9:
        return 0
    return dp[row][col][z]

def horseJump(x, y, step):
    return process(x, y, step)


def process(x, y, step):
    if x < 0 or x > 8 or y < 0 or y > 9:
        return 0
    if step == 0:
        return 1 if x == 0 and y == 0 else 0

    return process(x+1, y+2, step-1)+process(x+2, y+1, step-1)+process(x+2, y-1, step-1)\
    +process(x+1, y-2, step-1) + process(x-1, y-2,step-1)+process(x-2, y-1,step-1)\
    +process(x-2, y+1, step-1) + process(x-1, y+2, step-1)


def horseJumpDP(x, y, step):
    dp = [[[0 for i in range(step+1)]for i in range(10)] for i in range(9)]

    dp[0][0][0] = 1

    for k in range(1,step+1):

        for i in range(9):
            for j in range(10):
                dp[i][j][k] = getValue(dp, i+1, j+2, k-1)+getValue(dp, i+2,j+1,k-1)\
                              +getValue(dp, i+2, j-1,k-1)+getValue(dp, i+1, j-2,k-1)\
                              +getValue(dp,i-1,j-2,k-1)+getValue(dp,i-2,j-1, k-1)\
                              +getValue(dp,i-2,j+1,k-1)+getValue(dp,i-1,j+2,k-1)

    return dp[x][y][step]

def getValue(dp, x,y,k):
    if x<0 or x>8 or y<0 or y>9:
        return 0
    return dp[x][y][k]



if __name__ == '__main__':
    x = 7
    y = 7
    step = 10
    # print(horseJump(x,y,step))
    print(horseJumpDP(x,y,step))
    print(horseDP(x,y,step))