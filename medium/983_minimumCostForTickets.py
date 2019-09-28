import unittest
from typing import List

class Solution:
    '''
        AC
    '''
    def mincostTickets(self, days: List[int], costs: List[int])->int:
        inf = float('inf')
        '''
            dp[i] is the cost before and include day i
        '''
        dp = [inf]*(days[-1]+1)
        dp[days[0]-1] = 0

        for i in range(days[0], days[-1]+1):
            if i not in days:
                '''
                    Just record current total cost for querying by -7 or -30 operation.
                    Comparing dp[d] + cost(7) or dp[d] + cost(30) and dp[d]+cost(1) can
                    get total cost dp[d']

                                 d'-7
                                   |
                                   V 
                    ---d iiiiiiiiiiiiiiiii d' -----
                       |           |
                       V           V
                      dp[d]     ==dp[d]
                '''
                dp[i] = dp[i-1]
            else:
                '''
                    Move one day cost
                    ----*i-----
                '''
                slideOneDayCost = dp[i-1]+costs[0]
                '''
                    Add 7 days cost to the cost before 7 days is that total cost
                    include current day i by buying a 7 day pass at 7 days ago

                           { total cost     } => may be < cost(7d)
                    ---(i-7)--------------(i)-----
                         | {  or cost(7d)   }
                         V
                       dp[i-7] 
                '''
                slideSevenDayCost = costs[1] if i-7+1 < days[0] else dp[i-7+1-1]+costs[1]
                '''
                    Add 30 days cost to the cost before 30 days is that total cost
                    include current day i by buying a 30 day pass at 30 days ago

                            { total cost     } => may be < cost(30d)
                    ---(i-30)--------------(i)-----
                         | {  or cost(30d)   }
                         V
                       dp[i-30] 
                '''
                slideThirtyDayCost = costs[2] if i-30+1 < days[0] else dp[i-30+1-1]+costs[2]
                
                dp[i] = min(slideOneDayCost, slideSevenDayCost, slideThirtyDayCost)

        return dp[-1]

class Unittest_mincostTickets(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        days = [1,4,6,7,8,20]
        costs = [2,7,15]
        expected = 11
        self.assertEqual(expected, self.sol.mincostTickets(days, costs))

    def test_sample2(self):
        days = [1,4,6,7,8,12,13,14,15,20]
        costs = [2,7,15]
        expected = 15
        self.assertEqual(expected, self.sol.mincostTickets(days, costs))

    def test_sample3(self):
        days = [1,2,3,4,5,6,7,8,9,10,30,31]
        costs = [2,7,15]
        expected = 17
        self.assertEqual(expected, self.sol.mincostTickets(days, costs))

    def test_sample4(self):
        days = [8]
        costs = [2,7,15]
        expected = 2 
        self.assertEqual(expected, self.sol.mincostTickets(days, costs))

if __name__ == '__main__':
    unittest.main()
