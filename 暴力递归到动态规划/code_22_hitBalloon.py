#coding:utf-8
'''
@Time: 2020/3/23 20:51
@author: Tokyo
@file: code_22_hitBalloon.py
@desc:
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

说明:

你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:

输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/burst-balloons
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def maxScore(arr):
    if arr is None or arr == []:
        return 0
    arr = [1]+arr+[1]
    print(arr)
    return process(arr,1,len(arr)-2)


def process(arr,L, R):
    '''
    返回击破所有L到R范围上的气球所获得的最大分数
    假设L-1，R+1即范围外的都没有被击破
    :param arr:
    :param L:
    :param R:
    :return:
    '''
    if L==R:
        return arr[L]*arr[L-1]*arr[R+1]
    maxScore = 0
    # 依次讨论每个位置最后被击破的最大得分

    score = arr[L] * arr[L - 1] * arr[R + 1] + process(arr, L + 1, R)
    maxScore = max(maxScore, score)

    maxScore = max(maxScore, arr[R] * arr[L - 1] * arr[R + 1] + process(arr, L, R - 1))
    for i in range(L+1,R):
        maxScore = max(maxScore, arr[i]*arr[L-1]*arr[R+1]+process(arr,L,i-1)+process(arr,i+1,R))
    return maxScore

def maxScoreDP(arr):
    if arr is None or arr == []:
        return 0
    arr = [1]+arr+[1]
    n = len(arr)
    dp = [[0 for i in range(n)] for i in range(n)]
    for i in range(1,n-1):
        dp[i][i] = arr[i-1]*arr[i]*arr[i+1]

    for i in range(n-2,0,-1):
        for j in range(i+1,n-1):
            dp[i][j] = max(dp[i][j],arr[i-1]*arr[i]*arr[j+1]+dp[i+1][j])
            dp[i][j] = max(dp[i][j], arr[i-1]*arr[j]*arr[j+1]+dp[i][j-1])
            for k in range(i+1,j):
                dp[i][j] = max(dp[i][j], arr[i-1]*arr[k]*arr[j+1]+dp[i][k-1]+dp[k+1][j])

    return dp[1][n-2]
if __name__ == '__main__':
    arr = [35,16,83,87,84,59,48,41]
    print(maxScore(arr))
    print(maxScoreDP(arr))
