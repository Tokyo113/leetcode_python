#coding:utf-8
'''
@Time: 2019/12/9 15:13
@author: Tokyo
@file: code.py
@desc:
'''


class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None



def convert(arr):
    if arr is None or arr == []:
        return None
    return process(arr)


def process(arr):
    if arr == []:
        return None
    if len(arr) == 1:
        return Node(arr[0])


    mid = len(arr)>>1
    head = Node(arr[mid])
    head.left = process(arr[:mid])
    head.right = process(arr[mid+1:])

    return head

def travel(head):
    if head is None:
        return

    travel(head.left)
    print(head.val, end=" ")
    travel(head.right)



class Node2(object):
    def __init__(self):
        self.nexts = {}
        self.feature = None


def DT(dataframe):
    if i ==50:



    maxen = 0
    head = Node2()
    for i in dataframe.columns:
        info = entropy(dataframe,i, label)
        if info >maxen:
            maxen = info
            max_fea = i
    head.feature = max_fea
    for key, value in dataframe.groupby(max_fea).items():
        head.nexts[key] = DT(j.value)


def entropy(dataframe, i,label):
    pass




if __name__ == '__main__':
    a = []
    print(convert(a))
    travel(convert(a))
