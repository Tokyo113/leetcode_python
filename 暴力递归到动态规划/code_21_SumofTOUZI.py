#coding:utf-8
'''
@Time: 2020/3/18 17:03
@author: Tokyo
@file: code_21_SumofTOUZI.py
@desc:
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。



你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。



示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]


n 个骰子组成的数范围是n到6n，总共有6^n种可能
递归f（n,aim）返回n个骰子组成aim的方法数
很多数字重复计算了，改成动态规划
'''


def twoSum(n):
    res = []

    def process(n, aim):
        '''
        返回n个骰子组成aim的方法数
        '''
        if n == 1:
            return 1 if aim == 1 or aim == 2 or aim == 3 or aim == 4 or aim == 5 or aim == 6 else 0
        res = 0
        for i in range(1, min(7, aim)):
            res += process(n - 1, aim - i)

        return res

    for i in range(n, 6 * n + 1):
        res.append(process(n, i) / (6 ** n))
    return res

def twoSumDP(n):
    '''
    使用了空间压缩技巧，没必要使用二维表
    :param n:
    :return:
    '''
    if n<=0:
        return []
    dp = [0 for i in range(6*n+1)]
    for i in range(1,7):
        dp[i] = 1
    for i in range(2,n+1):
        for j in range(i*6, i-1,-1):
            dp[j] = 0

            for aim in range(1,7):
                if j <= aim:
                    break
                dp[j] += dp[j-aim]
        for j in range(i-1, -1,-1):
            dp[j] = 0
    res = dp[n:6*n+1]

    return [i/(6**n) for i in res]



if __name__ == '__main__':
    print(twoSum(3))
    print(twoSumDP(9))