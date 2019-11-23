#coding:utf-8
'''
@Time: 2019/11/19 10:41
@author: Tokyo
@file: code_01_RandomPool.py
@desc:
设计RandomPool结构
【题目】
设计一种结构，在该结构中有如下三个功能:
insert(key):将某个key加入到该结构，做到不重复加入
delete(key):将原本在结构中的某个key移除
getRandom(): 等概率随机返回结构中的任何一个key。
【要求】
Insert、delete和getRandom方法的时间复杂度都是O(1)

'''
import random
class Pool(object):
    def __init__(self):
        self.keyIndexMap = {}
        self.indexKeyMap = {}
        self.size = 0

    def insert(self, key):
        if self.keyIndexMap.get(key) == None:
            self.keyIndexMap[key] = self.size
            self.indexKeyMap[self.size] = key
            self.size += 1

    def delete(self, key):

        if len(self.keyIndexMap) == 0:
            return None
        removeIndex = self.keyIndexMap.get(key)
        lastIndex = self.size-1
        lastKey = self.indexKeyMap.get(lastIndex)
        self.keyIndexMap[lastKey] = removeIndex
        self.indexKeyMap[removeIndex] = lastKey
        self.keyIndexMap.pop(key)
        # index也要去掉，不然不是等概率
        self.indexKeyMap.pop(lastIndex)
        self.size -= 1

    def getRandom(self):
        if len(self.keyIndexMap) == 0:
            return
        randIndex = int(random.random()*self.size)
        return self.indexKeyMap.get(randIndex)





if __name__ == '__main__':
    pool = Pool()
    pool.insert("zuo")
    pool.insert("cheng")
    pool.insert("yun")
    pool.delete("zuo")
    # print(pool.getRandom())
    # print(pool.getRandom())
    # print(pool.getRandom())
    # print(pool.getRandom())
    # print(pool.getRandom())
    # print(pool.getRandom())


    print(pool.indexKeyMap)




