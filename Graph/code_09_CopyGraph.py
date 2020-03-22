#coding:utf-8
'''
@Time: 2020/3/22 17:37
@author: Tokyo
@file: code_09_CopyGraph.py
@desc:
给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

class Node {
    public int val;
    public List<Node> neighbors;
}
 

测试用例格式：

简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。该图在测试用例中使用邻接列表表示。

邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/clone-graph
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

这道题和链表的copy类似
用一个哈希表，key-原节点,value-新建的节点
然后遍历逐一连起来即可

'''

class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors



def copyGraph(node):
    if node is None:
        return None
    nodeMap = {}
    queue = []
    queue.append(node)
    nodeMap[node] = Node(node.val, [])
    while queue != []:
        ele = queue.pop(0)

        for i in ele.neighbors:
            if i not in nodeMap:
                nodeMap[i] = Node(i.val, [])
                queue.append(i)
            nodeMap.get(ele).neighbors.append(nodeMap.get(i))
    return nodeMap.get(node)


