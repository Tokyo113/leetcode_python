#coding:utf-8
'''
@Time: 2019/11/11 10:34
@author: Tokyo
@file: code_01_TrieTree.py
@desc:前缀树
'''

class TrieNode(object):
    def __init__(self):
        self.path = 0
        self.end = 0
        self.nexts = [None for i in range(26)]


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if word is None:
            return
        node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if node.nexts[index] is None:
                node.nexts[index] = TrieNode()
            node = node.nexts[index]
            node.path += 1
        node.end += 1

    def search(self, word):
        """
        word出现过几次
        :param word:
        :return:
        """
        if word is None:
            return 0
        node = self.root
        for i in range(len(word)):
            index = ord(word[i])-ord('a')
            if node.nexts[index] == None:
                return 0
            node = node.nexts[index]
        return node.end

    def prefixNumber(self, pre):
        """
        所有加入的字符串中有几个是以pre作为前缀的
        :param pre:
        """
        if pre is None:
            return 0
        node = self.root

        for i in range(len(pre)):
            index = ord(pre[i]) - ord('a')
            if node.nexts[index] == None:
                return 0
            node = node.nexts[index]
        return node.path

    def delete(self, word):
        if self.search(word) != 0:
            node = self.root

            for i in range(len(word)):
                index = ord(word[i]) - ord('a')
                node.nexts[index].path -= 1
                if node.nexts[index].path == 0:
                    node.nexts[index] = None
                    return
                node = node.nexts[index]
            node.end -= 1









if __name__ == '__main__':
    trie = Trie()
    print(trie.search("zuo"))
    trie.insert("zuo")
    print(trie.search("zuo"))
    trie.delete("zuo")
    print(trie.search("zuo"))
    trie.insert("zuo")
    trie.insert("zuo")
    trie.delete("zuo")
    print(trie.search("zuo"))
    trie.delete("zuo")
    print(trie.search("zuo"))
    trie.insert("zuoa")
    trie.insert("zuoac")
    trie.insert("zuoab")
    trie.insert("zuoad")
    trie.delete("zuoa")
    print(trie.search("zuoa"))
    print(trie.prefixNumber("zuo"))


