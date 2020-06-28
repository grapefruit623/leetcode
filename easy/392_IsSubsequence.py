# -*- coding:utf-8 -*-
import unittest

class Solution:
    '''
        AC
    '''
    def isSubsequence(self, s:str, t:str)->bool:
        dp = []
        for i in range(len(s)+1):
            dp.append([0]*(len(t)+1))
        
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = dp[i][j-1]

        return len(s) == dp[-1][-1]

class Unittest_isSubsequence(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        t = "ahbgdc"
        s = "abc"
        self.assertEqual(True, self.sol.isSubsequence(s,t))

    def test_sample2(self):
        t = "ahbgdc"
        s = "axc"
        self.assertEqual(False, self.sol.isSubsequence(s,t))

    def test_sample3(self):
        t = "ahbgdc"
        s = ""
        self.assertEqual(True, self.sol.isSubsequence(s,t))

    def test_sample4(self):
        t = ""
        s = ""
        self.assertEqual(True, self.sol.isSubsequence(s,t))

if __name__ == "__main__":
    unittest.main()
