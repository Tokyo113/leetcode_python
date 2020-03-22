#coding:utf-8
'''
@Time: 2020/3/20 13:17
@author: Tokyo
@file: code_08_isBinaryTree.py
@desc:
二叉树上有 n 个节点，按从 0 到 n - 1 编号，其中节点 i 的两个子节点分别是 leftChild[i] 和 rightChild[i]。

只有 所有 节点能够形成且 只 形成 一颗 有效的二叉树时，返回 true；否则返回 false。

如果节点 i 没有左子节点，那么 leftChild[i] 就等于 -1。右子节点也符合该规则。

注意：节点没有值，本问题中仅仅使用节点编号。



示例 1：



输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
输出：true
示例 2：



输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
输出：false
示例 3：



输入：n = 2, leftChild = [1,0], rightChild = [-1,-1]
输出：false


思路：
1.每个节点入度必须为1
2.有且只有一个入度为零的节点
3.BFS能全部遍历到

'''


def validateBinaryTreeNodes(n, leftChild, rightChild):
    import collections
    nextMap = collections.defaultdict(list)
    inMap = {}

    for i in range(n):
        nextMap[i].append(leftChild[i])
        nextMap[i].append(rightChild[i])
    for i in range(n):
        if leftChild[i] != -1:

            inMap[leftChild[i]] = inMap.get(leftChild[i], 0) + 1
            if inMap.get(leftChild[i]) >= 2:
                return False

        if rightChild[i] != -1:

            inMap[rightChild[i]] = inMap.get(rightChild[i], 0) + 1
            if inMap.get(rightChild[i]) >= 2:
                return False
    cnt = 0
    head = -1
    for i in range(n):
        if i not in inMap:
            cnt += 1
            head = i
    if cnt != 1 or head == -1:
        return False
    queue = []
    queue.append(head)
    res = []
    while queue != []:
        pp = queue.pop(0)
        res.append(pp)

        if nextMap.get(pp) != None:
            for i in nextMap.get(pp):
                if i != -1:
                    queue.append(i)
    print(res)
    return True if len(res) == n else False


if __name__ == '__main__':
    left = [1,-1,3,-1]
    right = [2,-1,-1,-1]
    print(validateBinaryTreeNodes(4,left,right))