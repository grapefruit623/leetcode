# -*- coding: utf-8 -*-
import unittest

class Solution:
    '''
        AC
    '''
    def numDecodings(self, s: str)->int:
        dp = [0]*len(s) 

        if int(s) == 0:
            return 0
        if len(s) == 1:
            if s[0] == '0':
                return 0
            else:
                return 1

        if len(s) >= 2:
            temp = int(s[0:2])
            if s[0] == '0':
                return 0
            else:
                if s[1] == '0' and temp > 26:
                    return 0
        dp[0] = 1
        dp[1] = 2 if int(s[0:2]) <= 26 and s[1] != '0' else 1

        for i in range(2, len(s)):
            temp = int(s[i-1:i+1])
            if temp == 0:
                return 0
            if temp > 26 and s[i] == '0':
                return 0
            if s[i-1] == '0':
                dp[i] = dp[i-1]
            else:
                if temp > 26:
                    dp[i] = dp[i-1]
                elif temp >= 1 and temp <= 26:
                    if s[i] == '0':
                        dp[i] = dp[i-2]
                    else:
                        dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]


class Unittest_numDecodings(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        data = "12"
        expected = 2
        self.assertEqual(expected, self.sol.numDecodings(data))

    def test_sample2(self):
        data = "226"
        expected = 3
        self.assertEqual(expected, self.sol.numDecodings(data))

    def test_sample3(self):
        data = "1221"
        expected = 5
        self.assertEqual(expected, self.sol.numDecodings(data))

    def test_sample4(self):
        data = "1228"
        expected = 3
        self.assertEqual(expected, self.sol.numDecodings(data))

    def test_sample5(self):
        data = "0"
        expected = 0
        self.assertEqual(expected, self.sol.numDecodings(data))

    def test_sample6(self):
        data = "1230"
        expected = 0
        self.assertEqual(expected, self.sol.numDecodings(data))

    def test_sample7(self):
        data = "1203"
        expected = 1
        self.assertEqual(expected, self.sol.numDecodings(data))

    def test_sample8(self):
        data = "03"
        expected = 0
        self.assertEqual(expected, self.sol.numDecodings(data))

    def test_sample9(self):
        data = "3000"
        expected = 0
        self.assertEqual(expected, self.sol.numDecodings(data))

    def test_sample10(self):
        data = "12020"
        expected = 1
        self.assertEqual(expected, self.sol.numDecodings(data))

    def test_sample11(self):
        data = "012"
        expected = 0
        self.assertEqual(expected, self.sol.numDecodings(data))

    def test_sample12(self):
        data = "10"
        expected = 1
        self.assertEqual(expected, self.sol.numDecodings(data))

if __name__ == '__main__':
    unittest.main()
