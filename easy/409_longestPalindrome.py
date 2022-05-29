# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        hashTable = {}
        ans = 0
        for c in s:
            if hashTable.get(c) != None:
                hashTable[c]+=1
            else:
                hashTable.setdefault(c,1)
            
        hasSingleChar=0
        for c in hashTable:
            ans+=2*(hashTable[c]//2)
            hashTable[c] -= 2*(hashTable[c]//2)
            
            if hashTable[c] == 1:
                hasSingleChar = 1
                
        ans += hasSingleChar
            
        return ans

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_case1(self):
        s="abccccdd"
        expect=7

        self.assertEqual(expect, self.sol.longestPalindrome(s))

    def test_case2(self):
        s="a"
        expect=1
        self.assertEqual(expect, self.sol.longestPalindrome(s))

    def test_case3(self):
        s="bb"
        expect=2
        self.assertEqual(expect, self.sol.longestPalindrome(s))

    def test_case4(self):
        s="ccc"
        expect=3
        self.assertEqual(expect, self.sol.longestPalindrome(s))

if __name__ == "__main__":
    unittest.main()
