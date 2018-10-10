# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest

"""
    AC
"""
class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mDict = []
        
    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.mDict.extend(dict)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one        character
        :type word: str
        :rtype: bool
        """

        for s in self.mDict:
            if len(s) == len(word):
                diffCount = 0
                for i in range(len(s)):
                    if s[i] != word[i]:
                        diffCount += 1

                if diffCount == 1:
                    return True

        return False

class Test_MagicDictionary(unittest.TestCase):
    def setUp(self):
        self.magicDictionary = MagicDictionary()

    def test_buildDictCase1(self):
        data = ["hello", "leetcode"]
        self.magicDictionary.buildDict(data)
        self.assertEqual(self.magicDictionary.mDict, data)

    def test_search_falseCase1(self):
        self.test_buildDictCase1()
        target = "hello"
        self.assertEqual(False, self.magicDictionary.search(target))

    def test_search_falseCase2(self):
        self.test_buildDictCase1()
        target = "hell"
        self.assertEqual(False, self.magicDictionary.search(target))

    def test_search_trueCase1(self):
        self.test_buildDictCase1()
        target = "hhllo"
        self.assertEqual(True, self.magicDictionary.search(target))


if __name__ == '__main__':
    unittest.main()
    '''
    suite1 = unittest.TestSuite()
    suite1 = Test_MagicDictionary("test_buildDictCase1")

    runner = unittest.TextTestRunner()
    runner.run(suite1)
    '''
