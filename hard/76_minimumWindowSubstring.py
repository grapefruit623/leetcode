# -*-coding: utf-8-*-
#! /usr/bin/python3
import unittest

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lenS = len(s)
        lenT = len(t)
        
        if lenS < lenT:
            return ""
        
        winS = 0
        winE = 0
        
        ans = ""
        minLen = lenS+1
        count = 0
        
        table = {}
        for c in t:
            if c not in table.keys():
                table[c] = 1
            else:
                table[c] += 1
        
        for winE in range(0, lenS):
            if s[winE] in table.keys():
                table[s[winE]] -= 1
                if table[s[winE]] >= 0:
                    count += 1 

            while count == lenT:
                if winE-winS+1 < minLen:
                    ans = s[winS:winE+1]
                    minLen = len(ans)
                    
                if s[winS] in table.keys():
                    table[s[winS]] += 1
                    if table[s[winS]] > 0:
                        count -= 1

                winS += 1                                
        return ans

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s="bba"
        t="ab"
        expect ="ba"
        self.assertEqual(expect, self.sol.minWindow(s,t))

    def test_case2(self):
        s="ADOBECODEBANC"
        t="ABC"
        expect ="BANC"
        self.assertEqual(expect, self.sol.minWindow(s,t))

if __name__ == "__main__":
    unittest.main()
