#coding:utf-8
'''
@Time: 2019/11/12 12:38
@author: Tokyo
@file: leetcode_0221_TrieTree.py
@desc:
'''


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


class Node(object):
    def __init__(self):
        self.path = 0
        self.end = 0
        self.nexts = [None for i in range(26)]


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        """
        if word is None:
            return
        node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if node.nexts[index] is None:
                node.nexts[index] = Node()
            node = node.nexts[index]
            node.path += 1
        node.end += 1

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.helper(word, self.root, 0)

    def helper(self, word, node, i):
        if i == len(word):
            return True if node.end != 0 else False

        if word[i] == '.':
            has = False
            # 遍历所有的nexts，都没有或者都为空才返回False
            for j in range(26):
                if node.nexts[j] != None:
                    if self.helper(word, node.nexts[j], i + 1):
                        return True
            return False
        else:
            index = ord(word[i]) - ord('a')
            if node.nexts[index] is None:
                return False
            node = node.nexts[index]
            return self.helper(word, node, i + 1)

