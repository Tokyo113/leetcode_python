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






def hanoi(n):
    return process1(n,'左','中','右')

def process1(n,from1,by,end):
    if n == 1:
        print('move'+str(n)+'from'+from1+'to'+end)
        return
    process1(n-1,from1,end,by)
    print('move'+str(n)+'from'+from1+'to'+end)
    process1(n-1,by,from1,end)






if __name__ == '__main__':
    hanoi(3)
    print('===')
    Hanoi(3)
