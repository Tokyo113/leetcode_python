#coding:utf-8
'''
@Time: 2020/4/8 10:19
@author: Tokyo
@file: code_22_二叉树的锯齿形遍历.py
@desc:
与层次遍历类似
使用双端队列
'''
class TreeNode():
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


import collections
def zigzagTree(head):
    if head is None:
        return []
    res = [[]]
    cur_end = head
    next_end = None
    queue = collections.deque()
    queue.append(head)
    flg = True
    while len(queue) != 0:
        print(queue)
        if flg:
            pp = queue.popleft()
            res[-1] += [pp.val]
            if pp.left != None:
                queue.append(pp.left)
                next_end = next_end if next_end != None else pp.left
            if pp.right != None:
                queue.append(pp.right)
                next_end = next_end if next_end != None else pp.right
        else:
            pp = queue.pop()
            res[-1] += [pp.val]
            if pp.right != None:
                queue.appendleft(pp.right)
                next_end = next_end if next_end != None else pp.right
            if pp.left != None:
                queue.appendleft(pp.left)
                next_end = next_end if next_end != None else pp.left
        if pp == cur_end:
            flg = not flg
            res.append([])
            cur_end = next_end
            next_end = None
    return res[:-1]

if __name__ == '__main__':
    head = TreeNode(3)
    head.left = TreeNode(9)
    head.right = TreeNode(20)
    head.right.left = TreeNode(15)
    head.right.right = TreeNode(7)
    print(zigzagTree(head))


