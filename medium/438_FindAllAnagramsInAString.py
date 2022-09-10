# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_charDict = {}

        for c in p:
            if c not in p_charDict:
                p_charDict[c] = 1
            else:
                p_charDict[c] += 1

        start = end = 0
        charDict = {}
        lenS = len(s)
        lenP = len(p)
        ans = []

        while end < lenS:

            if s[end] not in charDict:
                charDict[ s[end] ] = 1
            else:
                charDict[ s[end] ] += 1

            if end-start+1 == lenP:
                if charDict == p_charDict:
                    ans.append(start)

                if charDict[ s[start] ] == 1:
                    charDict.pop( s[start] )
                else:
                    charDict[ s[start] ] -= 1

                start += 1

            end += 1

        return ans

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_sample1(self):
        s = "cbaebabacd"
        p = "abc"
        expect = [0,6]

        self.assertEqual(expect, self.sol.findAnagrams(s, p))

    def test_sample2(self):
        s = "abab"
        p = "ab"
        expect = [0,1,2]

        self.assertEqual(expect, self.sol.findAnagrams(s, p))

if __name__ == "__main__":
    unittest.main()
        
