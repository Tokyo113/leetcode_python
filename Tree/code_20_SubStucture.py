#coding:utf-8
'''
@Time: 2020/3/9 18:36
@author: Tokyo
@file: code_20_SubStucture.py
@desc:
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：

0 <= 节点个数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
按层次遍历二叉树
当某一个头节点与子结构的头节点相同时，调用递归函数判断
其左右子树是否是完全相同
关键写出basecase
'''


def isSubStructure(self, A, B):
    if A is None or B is None:
        return False
    result = False
    queue = []
    queue.append(A)
    while queue != []:
        ele = queue.pop(0)
        if ele.val == B.val:
            tmp = self.match(ele.left, B.left) and self.match(ele.right, B.right)
            if tmp:
                return True
        else:
            # 当前节点不一样，继续遍历其他节点
            if ele.left != None:
                queue.append(ele.left)
            if ele.right != None:
                queue.append(ele.right)
    return result


def match(self, a, b):
    '''
    判断以a。b为头的树结构是否满足子结构关系
    :param self:
    :param a:
    :param b:
    :return:
    '''
    # 不管a是否为空，b为空了，肯定匹配成功了
    if b is None:
        return True
    # b还有结构，a空了，不成功
    if a is None:
        return False
    if a.val != b.val:
        return False
    else:
        return self.match(a.left, b.left) and self.match(a.right, b.right)