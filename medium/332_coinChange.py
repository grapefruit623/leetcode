# -*- coding: utf-8 -*-
import unittest
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int)->int:
        return self.coinChangeAC(coins, amount)

    '''
        AC
        dp[i] which means count of coins to reach amount i
        dp[i - c] which means count of coins to reach amount (i-c)

        if dp[i-c] is exists, there is a combination by coins to 
            get amount (i-c)

        The mean of dp[i-c] + 1 is equal count of coins to to reach amount i
        , because coin combination of i-coin can
        reach amount i just by add one coin which amount is c.

        dp[i] = min(dp[i], dp[i-c]+1) because sometime dp[i] == 1 if current
        amount is exists in coins list.

        time complexity is O(amount + len(coins))
    '''
    def coinChangeAC(self, coins: List[int], amount: int)->int:
        if amount == 0:
            return 0

        inf = float('inf')
        dp = [inf]*(amount+1)

        for i in range(amount+1):
            if i not in coins:
                for c in coins:
                    if i-c >= 0:
                        dp[i] = min(dp[i], dp[i-c]+1)
            else:
                dp[i] = 1
        
        return dp[amount] if dp[amount] != inf else -1

    '''
        Still TLE
    '''
    def coinChangeTLE2(self, coins: List[int], amount: int)->int:
        coins = sorted(coins)
        self.inf = float('inf')
        dp = {}
        for c in coins:
            upper = int(amount/c)
            for i in range(1, upper+1):
                if c*i in dp:
                    dp[c*i] = min(i, dp[c*i])
                else:
                    dp[c*i] = i

        self.ans = self.inf
        self.coinChangeTLE2_recursive(dp, sorted(list(dp.keys())), amount, 0, 0, 0)
        return self.ans

    def coinChangeTLE2_recursive(self, dp, keys, amount, counts, index, currentSum):
        if index >= len(keys):
            return True

        if currentSum == amount:
            self.ans = min(self.ans, counts)
        else:
            for i in range(index, len(keys)):
                if currentSum + keys[i] <= amount:
                    counts += dp[keys[i]]
                    currentSum += keys[i]

                    self.coinChangeTLE2_recursive(dp, keys, amount, counts, i+1, currentSum)

                    counts -= dp[keys[i]]
                    currentSum -= keys[i]
                else:
                    break
                    
        return False
    '''
        TLE
    '''
    def coinChangeTLE(self, coins: List[int], amount: int)->int:
        coins = sorted(coins)
        inf = float('inf')

        if amount == 0:
            return 0
        if amount < coins[0]:
            return -1

        dp = [inf]*(amount+1)
        minIndex = coins[0]

        for c in coins:
            if c > amount:
                break
            dp[c] = 1

        for di in range(minIndex, amount+1):
            i = minIndex
            middle = (i+di)/2
            if dp[di] == inf:
                while i <= middle:
                    if dp[i] != inf and dp[di-i] != inf:
                        dp[di] = min(dp[di], dp[i]+dp[di-i])
                    i += 1
        return dp[amount] if dp[amount] != inf else -1

class Unittest_coinChange(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        coins = [1,2,5]
        amount = 11
        self.assertEqual(3, self.sol.coinChange(coins, amount))

    def test_sample2(self):
        coins = [2]
        amount = 3 
        self.assertEqual(-1, self.sol.coinChange(coins, amount))

    def test_sample3(self):
        coins = [3]
        amount = 3 
        self.assertEqual(1, self.sol.coinChange(coins, amount))

    def test_sample4(self):
        coins = [5,7]
        amount = 13 
        self.assertEqual(-1, self.sol.coinChange(coins, amount))

    def test_sample5(self):
        coins = [5,7]
        amount = 12 
        self.assertEqual(2, self.sol.coinChange(coins, amount))

    def test_sample6(self):
        coins = [5,7]
        amount = 10 
        self.assertEqual(2, self.sol.coinChange(coins, amount))

    def test_sample7(self):
        coins = [1,5,7]
        amount = 4 
        self.assertEqual(4, self.sol.coinChange(coins, amount))

    def test_sample8(self):
        coins = [3,5,7]
        amount = 2 
        self.assertEqual(-1, self.sol.coinChange(coins, amount))

    def test_sample9(self):
        coins = [1]
        amount = 0 

    def test_sample10(self):
        coins = [1,2,5]
        amount = 6 
        self.assertEqual(2, self.sol.coinChange(coins, amount))

    def test_sample11(self):
        coins = [186,419,83,408]
        amount = 6249 
        self.assertEqual(20, self.sol.coinChange(coins, amount))

if __name__ == '__main__':
    unittest.main()
