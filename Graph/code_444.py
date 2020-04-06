#coding:utf-8
'''
@Time: 2020/4/1 20:48
@author: Tokyo
@file: code_444.py
@desc:
'''

#coding:utf-8
'''
@Time: 2020/4/1 19:46
@author: Tokyo
@file: code333.py
@desc:
'''


def topoSort(arr,find):
    import collections
    li = []
    fileMap = collections.defaultdict(list)
    inMap = {}
    zeroInQueue = []
    n = len(arr)
    for i in arr:
        a,b = i.split(':')
        for j in b.split(' '):
            fileMap[j].append(a)
            inMap[a] = inMap.get(a,0)+1
    for k,v in fileMap.items():
        if inMap.get(k) is None:
            zeroInQueue.append(k)
    cycle = False

    if zeroInQueue == []:
        cycle = True
        zeroInQueue.append(find)
        pp = []
        while zeroInQueue != []:
            ele = zeroInQueue.pop(0)
            pp.append(ele)

            # 最后一个节点没有next，所以不在courseMap中
            if fileMap.get(ele) != None:
                for i in fileMap.get(ele):
                    inMap[i] -= 1
                    if inMap.get(i) == 0:
                        zeroInQueue.append(i)
        res = pp[::-1]
        res = res[:-1]







    else:
        res = []
        while zeroInQueue != []:
            ele = zeroInQueue.pop(0)
            res.append(ele)

            # 最后一个节点没有next，所以不在courseMap中
            if fileMap.get(ele) != None:
                for i in fileMap.get(ele):
                    inMap[i] -= 1
                    if inMap.get(i) == 0:
                        zeroInQueue.append(i)
        if len(res) == n:
            cycle = False

    return cycle,res


if __name__ == '__main__':
    arr = ['a.h:b.h','b.h:c.h','c.h:a.h']
    print(topoSort(arr,'a.h')[1])
    a = topoSort(arr,'a.h')[1]
    print(' '.join(a))
