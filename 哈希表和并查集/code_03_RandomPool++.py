#coding:utf-8
'''
@Time: 2019/11/20 10:15
@author: Tokyo
@file: code_03_RandomPool++.py
@desc:
leetcode 381
设计一个支持在平均 时间复杂度 O(1) 下， 执行以下操作的数据结构。

注意: 允许出现重复元素。

insert(val)：向集合中插入元素 val。
remove(val)：当 val 存在时，从集合中移除一个 val。
getRandom：从现有集合中随机获取一个元素。每个元素被返回的概率应该与其在集合中的数量呈线性相关。


'''

'''
思路：
KeyMap 中放的不再是一个数，而是一个list，放所有的index
对list中的元素进行增删
'''
import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyIndexMap = {}
        self.indexKeyMap = {}
        self.size = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        hasVal = True if self.keyIndexMap.setdefault(val, []) == [] else False
        self.keyIndexMap.get(val).append(self.size)
        self.indexKeyMap[self.size] = val
        self.size += 1
        return hasVal

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.keyIndexMap.get(val) == None:
            return False

        removeIndex = self.keyIndexMap.get(val).pop(0)
        lastIndex = self.size - 1
        lastKey = self.indexKeyMap.get(lastIndex)
        self.keyIndexMap.get(lastKey).insert(0, removeIndex)
        self.keyIndexMap.get(lastKey).pop()

        if self.keyIndexMap.get(val) == []:
            self.keyIndexMap.pop(val)
        self.indexKeyMap[removeIndex] = lastKey
        self.indexKeyMap.pop(lastIndex)
        self.size -= 1
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        """
        rand = int(random.random() * self.size)
        return self.indexKeyMap.get(rand)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
    '''
["RandomizedCollection","insert","insert","insert","insert","insert","insert","remove","remove","remove","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
[[],[10],[10],[20],[20],[30],[30],[10],[10],[30],[30],[],[],[],[],[],[],[],[],[],[]]
    '''
    a = RandomizedCollection()
    print(a.insert(10))
    print(a.insert(10))
    print(a.insert(20))
    print(a.insert(20))
    print(a.insert(30))
    print(a.insert(30))
    print(a.keyIndexMap)
    print(a.indexKeyMap)
    # print(a.keyIndexMap)
    print(a.remove(10))
    print(a.indexKeyMap)
    print(a.keyIndexMap)
    print("===")

    print(a.remove(30))
    print(a.indexKeyMap)
    print(a.keyIndexMap)
    print("===")
    print(a.remove(10))
    # print(a.indexKeyMap)
    print(a.remove(30))
    print(a.indexKeyMap)


    print(a.getRandom())
    print(a.keyIndexMap)
    print(a.indexKeyMap)
    # print(a.remove(5))
    # print(a.keyIndexMap)