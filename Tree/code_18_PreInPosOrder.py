#coding:utf-8
'''
@Time: 2020/2/22 11:53
@author: Tokyo
@file: code_18_PreInPosOrder.py
@desc:
已知一棵二叉树中没有重复节点，并且给定了这棵树的中序遍历数组和先序遍历
数组，返回后序遍历数组。
比如给定：
int[] pre = { 1, 2, 4, 5, 3, 6, 7 };
int[] in = { 4, 2, 5, 1, 6, 3, 7 };
返回：
{4,5,2,6,7,3,1}
'''


def reconstruct(pre, ino):
    if pre is None or ino is None or len(pre) != len(ino) or pre == [] or ino == []:
        return []
    head = pre[0]
    i = ino.index(head)
    left = reconstruct(pre[1:i+1], ino[:i])
    right = reconstruct(pre[i+1:], ino[i+1:])
    return left+right+[head]


if __name__ == '__main__':

    pre = [1, 2, 4, 5, 3, 6, 7]
    ino = [4, 2, 5, 1, 6, 3, 7]
    print(reconstruct(pre,ino))
