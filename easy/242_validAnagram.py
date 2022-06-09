# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution:
    def isAnagram(self, s: str, t: str)->bool:
        if len(s) != len(t):
            return False

        hashTable={}
        for c in s:
            if c in hashTable:
                hashTable[c] += 1
            else:
                hashTable[c] = 1

        for c in t:
            if c in hashTable:
                hashTable[c] -= 1
            else:
                return False # Encount char which is not in s.

        for c in hashTable:
            if hashTable[c] != 0:
                return False # Amount of char c is not equal between s and t. 

        return True
        

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_case1(self):
        s="anagram"
        t="nagaram"
        expect=True
        self.assertEqual(expect, self.sol.isAnagram(s, t))

    def test_case2(self):
        s="rat"
        t="car"
        expect=False
        self.assertEqual(expect, self.sol.isAnagram(s, t))

if __name__ == "__main__":
    unittest.main()
