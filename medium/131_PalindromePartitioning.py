# -*-coding: utf-8 -*-
#! /usr/bin/python3
from typing import List
import unittest

'''
    AC
    Use dp to speed up.
'''
class Solution:
    def partition(self, s:str)->List[List[str]]:
        self.ans=[]
        self.s=s
        stack=[]

        '''
            Create DP array
            DP[i][j] == true means s[i:j] is palindrome
        '''

        self.dp=[]
        for j in range(0, len(s)):
            self.dp.append( [False]*len(s) )

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                isPal=self.checkIsPalindrome(s[i:j+1])
                self.dp[i][j] = isPal

        self.recursiveCheck(0, stack)
        return self.ans

    def recursiveCheck(self, start, stack):
        if start >= len(self.s):
            temp=[]
            for a in stack:
                temp.append(a)
            self.ans.append(temp)
            return

        for i in range(start, len(self.s)):
            IsSubPal=self.dp[start][i]
            if IsSubPal:
                stack.append(self.s[start:i+1])
                self.recursiveCheck(i+1, stack)
                stack.pop()

    def checkIsPalindrome(self, s:str)->bool:
        e=len(s)-1
        i=0
        while i < e:
            if s[i] != s[e]:
                return False
            i+=1
            e-=1
        return True


'''
    AC
    But recursive.
'''
class Solution_rec:
    def partition(self, s:str)->List[List[str]]:
        self.ans=[]
        self.s=s
        stack=[]

        self.recursiveCheck(0, stack)

        return self.ans


    def recursiveCheck(self, start, stack):
        if start >= len(self.s):
            temp=[]
            for a in stack:
                temp.append(a)
            self.ans.append(temp)
            return

        for i in range(start, len(self.s)):
            IsSubPal=self.checkIsPalindrome(self.s[start:i+1])
            if IsSubPal:
                stack.append(self.s[start:i+1])
                self.recursiveCheck(i+1, stack)
                stack.pop()

    def checkIsPalindrome(self, s:str)->bool:
        e=len(s)-1
        i=0
        while i < e:
            if s[i] != s[e]:
                return False
            i+=1
            e-=1
        return True


class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_case1(self):
        s="aab"
        expected=[["a","a","b"],["aa","b"]]
        self.assertEqual(expected, self.sol.partition(s))

    def test_case2(self):
        s="a"
        expected=[["a"]]
        self.assertEqual(expected, self.sol.partition(s))

    def test_case3(self):
        s="aaaa"
        expected=[["a","a","a","a"],["a","a","aa"],["a","aa","a"],["a","aaa"],["aa","a","a"],["aa","aa"],["aaa","a"],["aaaa"]]

        self.assertEqual(expected, self.sol.partition(s))

if __name__ == "__main__":
    unittest.main()



