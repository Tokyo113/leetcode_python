#coding:utf-8
'''
@Time: 2020/3/22 15:03
@author: Tokyo
@file: code_12_PathInMatrix.py
@desc:
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def hasPath(matrix, rows, cols, path):
    # write code here
    if matrix is None or matrix == []:
        return False

    def process(arr, i, j, index, path):
        # basecase 的先后也要注意，下面两条反了就不对
        if index == len(path):
            return True
        if i < 0 or j < 0 or i==rows or j==cols or arr[i][j] == -1:
            return False
        if arr[i][j] !=path[index]:
            return False
        tmp = arr[i][j]
        arr[i][j] = -1
        res = process(arr, i + 1, j, index + 1, path) or\
              process(arr, i - 1, j, index + 1, path) or \
              process(arr, i, j + 1, index+1,path) or \
              process(arr, i, j - 1, index + 1, path)
        if res:
            return True
        else:
            # 不行还要改回来，不然全是-1了
            arr[i][j] = tmp
            return False

    for i in range(rows):
        for j in range(cols):
            if process(matrix, i, j, 0, path):
                return True
    return False





if __name__ == '__main__':
    board = [['A', "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    boa = [['a','a','a']]
    word1 = 'aaa'
    word = "ABCCED"
    print(hasPath(boa,1,3,word1))



