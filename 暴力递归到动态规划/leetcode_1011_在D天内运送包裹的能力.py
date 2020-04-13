#coding:utf-8
'''
@Time: 2020/4/7 10:36
@author: Tokyo
@file: leetcode_1011_在D天内运送包裹的能力.py
@desc:
传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

 

示例 1：

输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。
示例 2：

输入：weights = [3,2,2,4,1,4], D = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4
示例 3：

输入：weights = [1,2,3,1,1], D = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def shipWithinDays(weights,D):
    if weights == [] or D <= 0:
        return

    def process(arr, i, res):
        '''
        返回在res天内运送arr[i:]货物的最小载重量
        :param arr:
        :param i:
        :param res:
        :return:
        '''
        if res < 0:
            return -1
        if res == 0:
            return 0 if i == len(arr) else -1
        if i == len(arr):
            return 0
        load = float('inf')
        for j in range(i, len(arr)):
            ans = process(arr, j + 1, res - 1)
            if ans == -1:
                continue
            # 取该种方案下每日运输量的最大值
            cur = max(sum(arr[i:j + 1]), ans)
            load = min(cur, load)
        return load

    return process(weights, 0, D)


def shipDaysDP(arr,days):
    '''
    超时，不是最优解
    :param arr:
    :param days:
    :return:
    '''
    if arr == [] or days<=0:
        return
    n = len(arr)
    dp = [[0 for i in range(days+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = -1 if i != n else 0
    for i in range(1,days+1):
        dp[n][i] = 0
    for j in range(1,days+1):
        for i in range(n-1,-1,-1):
            pp = 0
            dp[i][j] = float('inf')
            for k in range(i,n):
                pp += arr[k]
                ans = dp[k+1][j-1]
                if ans == -1:
                    continue
                cur = max(pp,ans)
                dp[i][j] = min(cur,dp[i][j])
    return dp[0][days]


def shipDays3(arr,days):
    '''
    最优解，二分查找最优的运载量
    :param arr:
    :param days:
    :return:
    '''
    if arr == [] or days <= 0:
        return
    start, end = max(arr), sum(arr)


    while start<end:
        print(start,end)
        mid = (start+end)//2
        can = check(arr,mid,days)
        if can:
            end = mid
        else:
            start = mid+1
    return end

def check(arr, cur, days):
    '''
    检查cur运载量是否满足要求
    :param arr:
    :param cur:
    :param days:
    :return:
    '''
    day = days
    cnt = 0
    for i in arr:
        cnt += i
        if i > cur:
            return False
        if cnt > cur:
            cnt = i
            day -= 1
    print(day)
    return True if day > 0 else False


if __name__ == '__main__':

    # print(shipDays3([1,2,3,4,5,6,7,8,9,10],5))
    print(check([1,2,3,4,5,6,7,8,9,10],15,5))
