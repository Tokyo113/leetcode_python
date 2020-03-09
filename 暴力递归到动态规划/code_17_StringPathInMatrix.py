#coding:utf-8
'''
@Time: 2020/3/6 21:46
@author: Tokyo
@file: code_17_StringPathInMatrix.py
@desc:
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。


'''


def exist(board, word):
    if board is None or board == []:
        return False
    visit = [[0 for i in range(len(board[0]))] for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):

            if process(board, i, j, 0, word, visit):
                return True



    return False


def process(board, i, j, index, word, visit):

    if index == len(word):
        return True

    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
        return False
    if visit[i][j] == 1:
        return False
    has = False

    if board[i][j] != word[index]:
        return False

    else:
        visit[i][j] = 1
        p1 = process(board, i + 1, j, index + 1, word, visit)
        p2 = process(board, i - 1, j, index + 1, word, visit)
        p3 = process(board, i, j + 1, index + 1, word, visit)
        p4 = process(board, i, j - 1, index + 1, word, visit)

        if p1 or p2 or p3 or p4:
            has = True
        else:
            visit[i][j] = 0


    return has

if __name__ == '__main__':
    strs = [['a', 'b']]
    print(exist(strs, 'ba'))
