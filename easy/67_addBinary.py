# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

'''
    AC
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxLen=max(len(a), len(b))
        a=a.zfill(maxLen)
        b=b.zfill(maxLen)
        add='0'
        ans=""

        for i in range(maxLen-1,-1,-1):
            currBit='0'
            if a[i]==b[i]:
                if a[i]=='1':
                    currBit=add
                    add='1'
                else:
                    currBit=add
                    add='0'
            else:
                if add=='1':
                    currBit='0'
                    add='1'
                else:
                    currBit='1'
                    add='0'
            ans+=currBit
        
        if add=='1':
            ans+='1'
        
        ans=ans[::-1]
        return ans
        
class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        a="11"
        b="1"
        expected="100"

        self.assertEqual(expected, self.sol.addBinary(a,b))

    def test_case2(self):
        a="1010"
        b="1011"
        expected="10101"

        self.assertEqual(expected, self.sol.addBinary(a,b))

    def test_case3(self):
        a="0"
        b="0"
        expected="0"

        self.assertEqual(expected, self.sol.addBinary(a,b))

if __name__ == "__main__":
    unittest.main()
