#coding:utf-8
'''
@Time: 2020/3/31 20:53
@author: Tokyo
@file: code_05_SubMatrixMaxSum.py
@desc:
给定一个正整数和负整数组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。

返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。

注意：本题相对书上原题稍作改动

示例:

输入:
[
   [-1,0],
   [0,-1]
]
输出: [0,1,0,1]
解释: 输入中标粗的元素即为输出所表示的矩阵

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-submatrix-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


思路：
和原题目一样，只不过想办法记录下标即可
'''


def getMaxMatrix(matrix):
    if matrix is None or matrix == []:
        return
    n, m = len(matrix), len(matrix[0])
    maxSum = float('-inf')
    res = [0, 0, 0, 0]
    for i in range(n):
        arr = [0 for i in range(len(matrix[0]))]
        for j in range(i, n):
            cur = 0
            for k in range(m):
                arr[k] += matrix[j][k]

                cur += arr[k]

                if cur > maxSum:

                    maxSum = cur

                    for p in range(k+1):
                        if sum(arr[p:k + 1]) == cur:

                            res = [i, p, j, k]
                            print(res)


                if cur < 0:
                    cur = 0


    return res

if __name__ == '__main__':
    arr = [[-1,0], [0,-1]]
    print(getMaxMatrix(arr))