# -*- coding:utf-8 -*-
import unittest

class Solution:
    '''
        AC
    '''
    def monotoneIncreasingDigits(self, N:int)->int:
        forward = last = len(str(N))-1
        nl = [ int(c) for c in str(N) ]
        '''
                 f'
                 |
                 v
            xxxxxxxxx
                ^   ^
                |   |
                f   l

            f' = f + 1
            if n[f] > n[f']:
                not monotone increasing
                n[f] -= 1 # decrease current highest digit
                replace all digit to 9 before f which is equal ( f ~ l)
        '''
        while forward >= 0:
            if forward < last and nl[forward] > nl[forward+1]:
                while last >= forward+1:
                    nl[last] = 9
                    last -= 1
                nl[forward] -= 1    
            forward -= 1

        return int("".join(str(c) for c in nl))

    '''
        TLE
        Force solution
    '''
    def TLE_monotoneIncreasingDigits(self, N:int)->int:
        while N > 0:
            result = self.checkingIsMonotoneIncreasing(N)
            if result == True:
                return N
            else:
                N -= 1
        return 0

    def checkingIsMonotoneIncreasing(self, n):
        ns = str(n)
        l = len(ns)

        for i in range(1, l):
            if ns[i-1] > ns[i]:
                return False

        return True

class unittest_monotoneIncreasingDigits(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        n = 332 
        self.assertEqual(299, self.sol.monotoneIncreasingDigits(n))

    def test_sample2(self):
        n = 1354 
        self.assertEqual(1349, self.sol.monotoneIncreasingDigits(n))

    def test_sample3(self):
        n = 10 
        self.assertEqual(9, self.sol.monotoneIncreasingDigits(n))

    def test_sample4(self):
        n = 1234 
        self.assertEqual(1234, self.sol.monotoneIncreasingDigits(n))

    def test_sample4(self):
        n = 11111 
        self.assertEqual(11111, self.sol.monotoneIncreasingDigits(n))

    def test_sample5(self):
        n = 984443 
        self.assertEqual(899999, self.sol.monotoneIncreasingDigits(n))

if __name__ == '__main__':
    unittest.main()
