#coding:utf-8
'''
@Time: 2019/11/15 11:43
@author: Tokyo
@file: code_01_Hanoi.py
@desc:
'''


def Hanoi(n):
    process(n, "左", "右", "中")


def process(i, start, end, other):
    if i == 1:
        print("move "+str(i)+' from '+start+' to '+end)
        return

    process(i-1, start, other, end)
    print("move "+str(i)+' from'+start+' to '+end)
    process(i-1, other, end, start)

if __name__ == '__main__':
    Hanoi(10)
