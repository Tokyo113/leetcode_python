#coding:utf-8
'''
@Time: 2020/2/22 11:20
@author: Tokyo
@file: code_04_Light.py
@desc:
小Q正在给一条长度为n的道路设计路灯安置方案。
为了让问题更简单,小Q把道路视为n个方格,需要照亮的地方用'.'表示, 不需要
照亮的障碍物格子用'X'表示。小Q现在要在道路上设置一些路灯, 对于安置在
pos位置的路灯, 这盏路灯可以照亮pos - 1, pos, pos + 1这三个位置。
小Q希望能安置尽量少的路灯照亮所有'.'区域, 希望你能帮他计算一下最少需
要多少盏路灯。
输入描述：
输入的第一行包含一个正整数t(1 <= t <= 1000), 表示测试用例数
接下来每两行一个测试数据, 第一行一个正整数n(1 <= n <= 1000),表示道路
的长度。第二行一个字符串s表示道路的构造,只包含'.'和'X'。
输出描述：
对于每个测试用例, 输出一个正整数表示最少需要多少盏路灯。

'''


def light1(strs):
    '''
    贪心策略解法
    :param strs:
    :return:
    '''
    if strs is None or strs == '':
        return 0
    i = 0
    res = 0
    while i < len(strs):
        if strs[i] == 'x':
            i += 1
        else:
            res += 1
            if i+1 == len(strs):
                break
            else:
                if strs[i+1] == 'x':
                    i += 2
                else:
                    i += 3
    return res


def light2(strs):
    '''
    动态规划解法
    :param strs:
    :return:
    '''
    if strs is None or strs == '':
        return 0
    return process(strs, 0)

def process(strs, i):
    if i >= len(strs):
        return 0

    if strs[i] == 'x':
        return process(strs, i+1)
    else:
        if i+1 == len(strs):
            return 1+process(strs, i+1)
        else:
            if strs[i+1] == 'x':
                return 1+process(strs, i+2)
            else: # 如果是.. 在i+1安灯，i+1两侧就不管了，直接i+3
                return 1+process(strs,i+3)





if __name__ == '__main__':
    strs = '.x.'
    print(light1(strs))
    print(light2(strs))
    print(light111(strs))

