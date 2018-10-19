# -*- coding: utf-8 -*-
#! /usr/bin/python3

import unittest

"""
    Use python's building method
    TLE
"""
class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.strList = []

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        "rtype: void
        """
        self.strList.append(word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word in self.strList:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        for s in self.strList:
            if s.startswith(prefix):
                return True

        return False

class Unittest_implementTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert(self):
        self.trie.insert("apple")
        self.assertEqual( ["apple"], self.trie.strList )

    def test_search(self):
        self.trie.insert("apple")
        result = self.trie.search("apple")
        self.assertEqual(True, result)

    def test_startsWith(self):
        self.trie.insert("apple")
        result = self.trie.startsWith("app")
        self.assertEqual(True, result)

    def tearDown(self):
        self.trie = None

if __name__ == "__main__":
    unittest.main()

