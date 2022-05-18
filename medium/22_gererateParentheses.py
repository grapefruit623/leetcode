# -*-coding: utf-8-*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    def generateParentheses(self, n:int)->List[str]:
        leftRemainCount=n
        rightRemainCount=n
        self.ans=[]
        self.currentPar=[]

        self.recursiveHelp(leftRemainCount, rightRemainCount)

        return self.ans

    def recursiveHelp(self, l, r):
        if r < l:
            return

        if l == 0 and r == 0:
            a="".join(self.currentPar)
            print ('a: ', a)
            self.ans.append(a)

        if l > 0:
            self.currentPar.append('(')
            self.recursiveHelp(l-1, r)
            self.currentPar.pop()
        if r > 0:
            self.currentPar.append(')')
            self.recursiveHelp(l, r-1)
            self.currentPar.pop()
        

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_case1(self):
        inp=3
        expect=["((()))","(()())","(())()","()(())","()()()"]
        self.assertEqual(expect, self.sol.generateParentheses(inp))

if __name__ == "__main__":
    unittest.main()


