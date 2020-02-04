#coding:utf-8
'''
@Time: 2020/2/3 21:01
@author: Tokyo
@file: code_02_AppleMinBags.py
@desc:
小虎去附近的商店买苹果，奸诈的商贩使用了捆绑交易，只提供6个每袋和8个
每袋的包装包装不可拆分。可是小虎现在只想购买恰好n个苹果，小虎想购买尽
量少的袋数方便携带。如果不能购买恰好n个苹果，小虎将不会购买。输入一个
整数n，表示小虎想购买的个苹果，返回最小使用多少袋子。如果无论如何都不
能正好装下，返回-1。
'''

def minBags(n):
    '''
    先写出笨方法，打印出来结果总结数学规律
    :param n:
    :return:
    '''
    if n <= 0 or n%2 != 0:
        return -1

    bags8 = n // 8
    restApple = n - 8*bags8
    bags6 = -1

    while restApple >= 0 and restApple < 24:
        if restApple % 6 == 0:
            bags6 = restApple // 6
            break
        if bags8 == 0:
            break
        bags8 -= 1
        restApple = n-8*bags8


    return bags8+bags6 if bags6 != -1 else -1

def minBags2(n):
    if n <= 0 or n % 2 != 0:
        return -1
    for i in range(n, -1, -1):
        for j in range(n):
            if 8*i+6*j == n:
                return i+j

    return -1


def minBags3(n):
    '''
    最优解，数学规律
    :param n:
    :return:
    '''
    if n % 2 != 0 or n <= 5:
        return -1
    if n < 18:
        if n == 6 or n == 8:
            return 1
        elif n == 12 or n == 14 or n == 16:
            return 2
        else:
            return -1

    else:
        return (n-18) // 8 + 3



if __name__ == '__main__':
    for n in range(100):
        a = minBags(n)
        b = minBags3(n)

        if a != b:
            print(n, a,b)
            print("fucking fucked!!!")



