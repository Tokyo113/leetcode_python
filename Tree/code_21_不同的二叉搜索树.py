#coding:utf-8
'''
@Time: 2020/4/1 21:58
@author: Tokyo
@file: code_21_不同的二叉搜索树.py
@desc:
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def generateTrees(n):
    if n <= 0:
        return []
    arr = [i for i in range(1, n + 1)]

    def process(arr):
        if arr == []:
            return None
        res = []
        for i in range(len(arr)):
            head = TreeNode(arr[i])
            left = process(arr[:i])
            right = process(arr[i + 1:])
            if left is None and right is None:
                head.left = None
                head.right = None
                res.append(head)
            elif left is None:
                head.left = None
                for i in right:
                    head.right = i
                    res.append(head)
            elif right is None:
                head.right = None
                for i in left:
                    head.left = i
                    res.append(head)
            else:
                for i in left:
                    for j in right:
                        head.left = i
                        head.right = j
                        res.append(head)
        return res

    return process(arr)

def travel(head):
    if head is None:
        return
    print(head.val, end=' ')
    travel(head.left)
    travel(head.right)

if __name__ == '__main__':
    res = generateTrees(3)
    print(res)
    for i in res:
        travel(i)
        print('')