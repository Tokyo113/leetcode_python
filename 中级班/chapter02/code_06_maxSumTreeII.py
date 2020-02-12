#coding:utf-8
'''
@Time: 2020/2/12 17:19
@author: Tokyo
@file: code_06_maxSumTreeII.py
@desc:
leetcode124
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

分析：最大路径可能出现在左子树+头+右子树一长条，也可能只在左子树或者右子树之中
而且要注意负数，负数节点对于代求指标贡献为负，可直接忽略，不加更好

如果统一返回最大路径和的话，没法判断是哪种情况，不能贸然加上头节点
所以还像前一题，process函数只记录叶节点到根节点的最大和，
再定义一个全局变量，尝试计算左+右+头，看是否能增大，最后结果记录在这个全局变量中
对于负数的话，process函数直接返回0，表示舍弃这个节点
'''
class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
maxS = float('-inf')
def maxSum(head):
    if head is None:
        return




    def process(head):
        global maxS
        if head is None:
            return 0

        left = process(head.left)
        right = process(head.right)
        tmp = max(left, right)+head.val
        maxS = max(maxS, left+right+head.val)
        return tmp if tmp > 0 else 0
    process(head)
    return maxS

if __name__ == '__main__':
    head = Node(-10)
    head.left = Node(-9)
    head.right = Node(-20)
    head.right.left = Node(-15)
    head.right.right = Node(-7)
    print(maxSum(head))