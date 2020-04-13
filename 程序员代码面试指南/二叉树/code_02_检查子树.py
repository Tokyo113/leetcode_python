#coding:utf-8
'''
@Time: 2020/4/9 11:26
@author: Tokyo
@file: code_02_检查子树.py
@desc:
leetcode 04.10
检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。

如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。

示例1:

 输入：t1 = [1, 2, 3], t2 = [2]
 输出：true
示例2:

 输入：t1 = [1, null, 2, 4], t2 = [3, 2]
 输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-subtree-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

即要求从t1某个节点往下与t2完全相同，不能多也不能少
不同于子结构

两种方法：
1.O(N*M):遍历t1每一个节点，然后遍历t2看是否满足
2.O(N+M):序列化转化为字符串找子串问题，KMP,最优解
序列化t1 O(N),t2 O(M),KMP  O(M+N)===>总的时间复杂度O(M+N)

这道题说明了非常大的二叉树，显然不能用第一种方法了哦！

'''

class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def subTree(head1,head2):
    '''
    遍历t1每个节点判断是否满足
    :param head1:
    :param head2:
    :return:
    '''
    if head1 is None or head2 is None:
        return False
    def process(node1,node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        return process(node1.left, node2.left) and process(node1.right,node2.right)



    queue = []
    queue.append(head1)
    while queue != []:
        pp = queue.pop(0)
        if process(pp,head2):
            return True
        if pp.left != None:
            queue.append(pp.left)
        if pp.right != None:
            queue.append(pp.right)
    return False


def subTree1(head1,head2):
    '''
    最优解，O(M+N)
    :param head1:
    :param head2:
    :return:
    '''
    if head1 is None or head2 is None:
        return False
    strs1 = serielize(head1)
    strs2 = serielize(head2)
    print(strs1,strs2)
    return True if KMP(strs1,strs2) != -1 else False

def serielize(node):
    '''
    先序遍历序列化（本题不能用层次遍历）
    :param node:
    :return:
    '''
    if node is None:
        return '#!'
    return str(node.val)+'!'+serielize(node.left)+serielize(node.right)

def KMP(s1,s2):
    if len(s2)>len(s1):
        return -1
    if s1 == s2:
        return 0
    nextArr = getNextArr(s2)
    i1,i2 = 0, 0
    while i1 < len(s1) and i2 <len(s2):
        if s1[i1] == s2[i2]:
            i1 += 1
            i2 += 1
        else:
            if i2 == 0:
                i1 += 1
            else:
                i2 = nextArr[i2]
    return i1-i2 if i2 == len(s2) else -1

def getNextArr(s):

    arr  = [0 for i in range(len(s))]
    arr[0] = -1
    arr[1] = 0
    i = 2
    cn = 0
    while i < len(s):
        if s[cn] == s[i-1]:
            arr[i] = cn+1
            cn += 1
            i += 1
        else:
            if cn>0:
                cn = arr[cn]
            else:
                arr[i] = 0
                i += 1
    return arr
if __name__ == '__main__':
    head1 = TreeNode(1)
    head1.left = TreeNode(2)
    head1.right = TreeNode(3)
    head2 = TreeNode(2)
    print(subTree1(head1,head2))



