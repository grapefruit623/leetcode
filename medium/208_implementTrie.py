# -*- coding: utf-8 -*-
#! /usr/bin/python3

import unittest

"""
    2018/10/19:
        Use python's building method
        TLE
        Remember this question's title: trie!
        trie is tree data structure.

    2018/10/20:
        AC
        Implement a simple trie 
"""
class Trie:
    
    class TrieNode():
        def __init__(self, word):
            self.char = word
            self.childs = {}
            self.count = 0

        def __repr__(self):
            return str(self.char) +"- "+ str(self.childs)


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        "rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.childs:
                node.childs[c] = self.TrieNode(c)

            node = node.childs[c]

        node.count = 1

    def search(self, word, isStartWith=False):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node.childs:
                return False
            else:
                node = node.childs[c]

        if not isStartWith and node.count == 0:
            return False

        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.search(prefix, isStartWith=True)

class Unittest_implementTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert(self):
        self.trie.insert("apple")
        self.assertEqual(None, self.trie.root.char)
        self.assertEqual("a", self.trie.root.childs['a'].char)
        self.assertEqual("p", self.trie.root.childs['a'].childs['p'].char)
        self.assertEqual("p", self.trie.root.childs['a'].childs['p'].childs['p'].char)
        self.assertEqual("l", self.trie.root.childs['a'].childs['p'].childs['p'].childs['l'].char)
        self.assertEqual("e", self.trie.root.childs['a'].childs['p'].childs['p'].childs['l'].childs['e'].char)

    def test_search(self):
        self.trie.insert("apple")
        result = self.trie.search("apple")
        self.assertEqual(True, result)

    def test_search_fail(self):
        self.trie.insert("apple")
        result = self.trie.search("app")
        self.assertEqual(False, result)

    def test_startsWith(self):
        self.trie.insert("apple")
        result = self.trie.startsWith("app")
        self.assertEqual(True, result)

    def test_wa_case1(self):
        self.trie.insert("apple")
        self.assertEqual(True, self.trie.search("apple"))
        self.assertEqual(False, self.trie.search("app"))
        self.assertEqual(True, self.trie.startsWith("app"))
        self.trie.insert("app")
        self.assertEqual(True, self.trie.search("app"))

    def tearDown(self):
        self.trie = None

if __name__ == "__main__":
    unittest.main()

