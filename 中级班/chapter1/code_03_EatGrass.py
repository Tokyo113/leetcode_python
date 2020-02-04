#coding:utf-8
'''
@Time: 2020/2/4 12:11
@author: Tokyo
@file: code_03_EatGrass.py
@desc:
'''

def winner(n):
    if n == 0:
        return "后手"
    a_eat = 1

    while n-a_eat >= 0:
        if winner(n-a_eat) == "后手":
            return "先手"

        if a_eat > n // 4:
            break

        a_eat = a_eat*4

    return "后手"

def winner2(n):
    if n%5 == 0 or n%5 == 2:
        return "后手"
    else:
        return "先手"
if __name__ == '__main__':
    for n in range(50):
        a = winner(n)
        b = winner2(n)

        if a != b:
            print("fucking fucked")



