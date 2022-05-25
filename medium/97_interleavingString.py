# -*- coding:utf-8 -*-
#! /usr/bin/python3

import unittest

'''
    AC

    ref: https://medium.com/@bill800227/leetcode-97-interleaving-string-18b1202fb0ea
'''
class Solution:
    def isInterleave(self, s1:str, s2:str, s3:str)->bool:
        slen1 = len(s1)
        slen2 = len(s2)
        slen3 = len(s3)

        if s1=="" and s2=="" and s3=="":
            return True

        if slen1+slen2 != slen3:
            return False
        
        '''
            Definition of dp[i][j] is
            s1[0:j+1] and s2[0:i+1] can combine to s3[0: i+j]

            For example

            dp[0][1] means s1[0:2] is substring of s3.
        '''
        dp=[]
        for i in range(0, slen2+1):
            dp.append( [False]*(slen1+1) )

        dp[0][0] = True
        for i in range(1, slen2+1):
            if s2[i-1] == s3[i-1] and dp[i-1][0] == True:
                dp[i][0] = True

        for j in range(1, slen1+1):
            if s1[j-1] == s3[j-1] and dp[0][j-1] == True:
                dp[0][j] = True

        for i in range(1, slen2+1):
            for j in range(1, slen1+1):
                if dp[i][j-1] == False and dp[i-1][j] == False:
                    dp[i][j] = False
                elif dp[i][j-1] == True and s1[j-1] != s3[i+j-1]:
                    dp[i][j] = False
                elif dp[i-1][j] == True and s2[i-1] != s3[i+j-1]:
                    dp[i][j] = False
                else:
                    '''
                        dp[i][j-1] and s1[j-1] which means

                        dp[i][j-1] == True means that
                        s2[0:i+1] combine s1[0:j-2] can to create s3[0:i+j-2]

                        Try to concatenate a new char from s1, it index is j-1

                        If new char from s1 is equals char from s3's current end
                        then a valid string borned.

                    '''
                    if dp[i][j-1] == True and s1[j-1] == s3[i+j-1]:
                        dp[i][j] = True
                    if dp[i-1][j] == True and s2[i-1] == s3[i+j-1]:
                        dp[i][j] = True

        return dp[-1][-1]

class Unittest(unittest.TestCase):
    def setUp(self):
        self.sol=Solution()

    def test_case1(self):
        s1="aabcc"
        s2="dbbca"
        s3="aadbbcbcac"
        expect=True

        self.assertEqual(expect, self.sol.isInterleave(s1, s2, s3))

    def test_case2(self):
        s1=""
        s2=""
        s3=""
        expect=True
        self.assertEqual(expect, self.sol.isInterleave(s1, s2, s3))

    '''
        WA
    '''
    def test_case3(self):
        s1="a"
        s2=""
        s3="aa"
        expect=False
        self.assertEqual(expect, self.sol.isInterleave(s1, s2, s3))

    '''
        WA
    '''
    def test_case4(self):
        s1="db"
        s2="b"
        s3="cbb"
        expect=False
        self.assertEqual(expect, self.sol.isInterleave(s1, s2, s3))

if __name__ == "__main__":
    unittest.main()


