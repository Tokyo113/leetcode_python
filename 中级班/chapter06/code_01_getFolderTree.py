#coding:utf-8
'''
@Time: 2020/2/21 10:55
@author: Tokyo
@file: code_01_getFolderTree.py
@desc:
给你一个字符串类型的数组arr，譬如：
String[] arr = { "b\\cst", "d\\", "a\\d\\e", "a\\b\\c" };
你把这些路径中蕴含的目录结构给画出来，子目录直接列在父目录下面，并比父目录
向右进两格，就像这样:
a
  b
    c
  d
    e
b
  cst
d
同一级的需要按字母顺序排列，不能乱。

思路：前缀树+深度优先遍历
'''

class Node(object):
    def __init__(self, s):
        self.str = s
        self.nexts = {}

def getFolderTree(arr):
    if arr is None or arr == []:
        return
    head = getTree(arr)
    printProcess(head, 0)


def getTree(arr):
    root = Node('')
    for i in arr:
        words = i.split('\\')
        cur = root
        for ele in words:
            if cur.nexts.get(ele) is None:
                cur.nexts[ele] = Node(ele)
            cur = cur.nexts[ele]
    return root

def  printProcess(node, level):
    if level != 0:
        print(getSpace(level)+node.str)
    for pp in node.nexts.values():
        printProcess(pp, level+1)

def getSpace(n):
    res = ''
    for i in range(1,n):
        res += '  '
    return res


if __name__ == '__main__':
    arr = ["b\\cst", "d\\q", "a\\d\\e", "a\\b\\c"]
    getFolderTree(arr)

