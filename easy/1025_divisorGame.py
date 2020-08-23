#-*- coding:utf-8
import unittest

class Solution:
    def divisorGame(self, N: int)->bool:
        if N == 1:
            return False
        if N == 2:
            return True

        dp = [False]*(N+1)
        dp[0] = False
        dp[1] = False
        dp[2] = True

        for i in range(1, N+1):
            for j in range(1, i):
                if i%j == 0 :
                    if dp[i-j] == False:
                        dp[i] = True
        return dp[N]

class Unittest_divisorGame(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        n = 2
        expected = True
        self.assertEqual(expected, self.sol.divisorGame(n))

    def test_sample2(self):
        n = 3
        expected = False
        self.assertEqual(expected, self.sol.divisorGame(n))

    def test_sample3(self):
        n = 4
        expected = True
        self.assertEqual(expected, self.sol.divisorGame(n))

if __name__ == '__main__':
    unittest.main()

