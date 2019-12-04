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



class Node(object):
    def __init__(self):
        self.path = 0
        self.end = 0
        self.next = [None for i in range(26)]


class qianzhuishu(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        if word is None:
            return
        node = self.root
        for i in range(len(word)):
            index = ord(word[i])-ord('a')
            if node.next[index] == None:
                node.next[index] = Node()
            node = node.next[index]
            node.path += 1
        node.end += 1

    def search(self, word):
        if word is None:
            return 0
        node = self.root
        for i in range(len(word)):
            index = ord(word[i])-ord('a')
            if node.next[index] == None:
                return 0
            node = node.next[index]
        return node.end

    def qianzhui(self, word):
        if word is None:
            return 0
        node = self.root
        for i in range(len(word)):
            index = ord(word[i])-ord('a')
            if node.next[index] == None:
                return 0
            node = node.next[index]
        return node.path

    def delete(self, word):
        if self.search(word) == 0:
            return

        node = self.root
        for i in range(len(word)):
            index = ord(word[i])-ord('a')
            node.next[index].path -= 1
            if node.next[index].path == 0:
                node.next[index] = None
                return
            node = node.next[index]
        node.end -= 1




'''
前缀树拓展：leetcode211
设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
说明:

你可以假设所有单词都是由小写字母 a-z 组成的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-and-search-word-data-structure-design
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


'''



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

    print("=="*50)

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
    print("========================")
    tree = qianzhuishu()
    tree.insert('abc')
    tree.insert('abf')
    tree.delete('abc')
    print(tree.search('ab'))
    print(tree.qianzhui('ab'))




