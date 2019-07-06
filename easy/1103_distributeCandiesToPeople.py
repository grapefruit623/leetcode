# -*- coding:utf-8 -*-
import unittest
from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int)->List[int]:
        '''
            1 + 2 + 3 +.... n <= candies
            n(n+1)
            ------  <= candies
              2
        '''
        n = -1
        lastRemainCandies = 0
        for i in range(candies):
            if i*(i+1)/2 > candies:
                n = i-1
                lastRemainCandies = candies - n*(n+1)/2
                break
        
        rows = int(n/num_people)
        remains = n % num_people

        ans = []

        '''
            p p p p p
            s s s
        '''
        pri = rows*(rows+1)/2
        sec = (rows-1)*(rows)/2

        for i in range(num_people):
            cont = i + 1
            if i < remains:
                sentCandies = pri*num_people + (rows+1)*cont
            elif i == remains:
                sentCandies = sec*num_people + (rows)*cont + lastRemainCandies
            else:
                sentCandies = sec*num_people + (rows)*cont

            ans.append( int(sentCandies) )

        return ans

class unittest_distributeCandies(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        candies = 10 
        num_people = 3
        expected = [5,2,3]
        self.assertEqual(expected, self.sol.distributeCandies(candies, num_people))

    def test_sample2(self):
        candies = 7 
        num_people = 4
        expected = [1,2,3,1]
        self.assertEqual(expected, self.sol.distributeCandies(candies, num_people))

    def test_sample3(self):
        candies = 10 
        num_people = 2
        expected = [4,6]
        self.assertEqual(expected, self.sol.distributeCandies(candies, num_people))

    def test_sample4(self):
        candies = 10 
        num_people = 1
        expected = [10]
        self.assertEqual(expected, self.sol.distributeCandies(candies, num_people))

    def test_sample5(self):
        candies = 15 
        num_people = 3
        expected = [5,7,3]
        self.assertEqual(expected, self.sol.distributeCandies(candies, num_people))

    def test_sample6(self):
        candies = 16 
        num_people = 3
        expected = [5,7,4]
        self.assertEqual(expected, self.sol.distributeCandies(candies, num_people))

if __name__ == '__main__':
    unittest.main()
