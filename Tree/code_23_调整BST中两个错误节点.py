#coding:utf-8
'''
@Time: 2020/4/8 11:08
@author: Tokyo
@file: code_23_调整BST中两个错误节点.py
@desc:
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

1.请找出这两个错误的节点
中序遍历找到升序的部分
有两种情况
1.第一次出现升序的较大的节点
2.最后一次出现升序的较小的节点



2.交换这两个节点，恢复BST结构（不能交换val值来实现）
14种情况
'''
class TreeNode():
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

def findError(head):
    '''
    简化问题：找到两个错误的节点
    然后交换值即可
    :param head:
    :return: [node1,node2]
    '''
    if head is None:
        return
    res = [None,None]
    stack = []
    cur = head
    new = head
    pre = None
    while head != None or stack != []:
        if head != None:
            stack.append(head)
            head = head.left
        else:
            pp = stack.pop()
            if pre != None and pp.val < pre.val:
                res[0] = res[0] if res[0] != None else pre
                res[1] = pp
            pre = pp
            head = pp.right
    res = [i.val for i in res]
    while cur != None or stack != []:
        if cur != None:
            stack.append(cur)
            cur = cur.left
        else:
            pp = stack.pop()

            if pp.val == res[0]:
                pp.val = res[1]
            elif pp.val == res[1]:
                pp.val = res[0]


            cur = pp.right

    return new

def travel(head):
    if head is None:
        return
    travel(head.left)
    print(head.val, end=' ')
    travel(head.right)




if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(3)
    head.left.right = TreeNode(2)
    print(travel(findError(head)))

