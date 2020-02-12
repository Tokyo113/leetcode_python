#coding:utf-8
'''
@Time: 2020/2/12 13:34
@author: Tokyo
@file: code_15_ReconstructTree.py
@desc:
leetcode105
根据一棵树的前序遍历与中序遍历构造二叉树。


进阶：leetcode1008
只从先序遍历重建一棵二叉搜索树
一样的，对先序遍历进行sort就得到了中序遍历
注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def reconstruct(preorder, inorder):
    if preorder == [] or inorder == []:
        return
    value = preorder[0]
    head = Node(value)
    i = inorder.index(value)
    left_in = inorder[:i]
    right_in = inorder[i+1:]
    left_pre = preorder[1:i+1]
    right_pre = preorder[i+1:]
    head.left = reconstruct(left_pre, left_in)
    head.right = reconstruct(right_pre, right_in)
    return head

def buildTree(inorder, postorder):
    '''
    从后序遍历和中序遍历重建二叉树
    :param inorder:
    :param postorder:
    :return:
    '''
    if inorder == [] or postorder == []:
        return
    value = postorder[-1]
    i = inorder.index(value)
    head = Node(value)
    head.left = buildTree(inorder[:i], postorder[:i])
    head.right = buildTree(inorder[i + 1:], postorder[i:-1])
    return head
def travel(head):
    if head is None:
        return
    print(head.val, end=' ')
    travel(head.left)
    travel(head.right)
if __name__ == '__main__':
    pre = [1,2,4,8,5,3,6,7]
    ino = [8,4,2,5,1,6,3,7]
    travel(reconstruct(pre, ino))


    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    travel(buildTree(inorder, postorder))



