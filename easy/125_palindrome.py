# -*- coding:utf-8 -*-
#! /usr/bin/python3
import unittest
import re

class Solution:
    def isPalindrome(self, s: str)->bool:
        s=s.lower()
        s=re.sub('[^a-z0-9]', '', s)

        print(s)

        i=0
        j=len(s)-1

        while i<j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        
    def test_case1(self):
        s = "A man, a plan, a canal: Panama"
        expected=True
        self.assertEqual(expected, self.sol.isPalindrome(s))

    def test_case2(self):
        s = " "
        expected=True
        self.assertEqual(expected, self.sol.isPalindrome(s))

    '''
        Is wa case.
    '''
    def test_case3(self):
        s = "0P"
        expected=False
        self.assertEqual(expected, self.sol.isPalindrome(s))

if __name__ == "__main__":
    unittest.main()
