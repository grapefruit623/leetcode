# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str)->bool:
        hashTable={}

        for c in magazine:
            if c not in hashTable:
                hashTable[c] = 1
            else:
                hashTable[c] += 1

        for c in ransomNote:
            if c not in hashTable:
                return False
            elif hashTable[c] == 0:
                return False
            else:
                hashTable[c] -= 1

        return True

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_case1(self):
        inp="a"
        mag="b"
        self.assertEqual(False, self.sol.canConstruct(inp, mag))

    def test_case2(self):
        inp="aa"
        mag="ab"
        self.assertEqual(False, self.sol.canConstruct(inp, mag))

    def test_case3(self):
        inp="aa"
        mag="aab"
        self.assertEqual(True, self.sol.canConstruct(inp, mag))

if __name__ == "__main__":
    unittest.main()
