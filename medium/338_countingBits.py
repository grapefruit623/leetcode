import unittest
from typing import List

class Solution:
    '''
        AC
    '''
    def countBits(self, num: int)->List[int]:
        power = 1
        '''
            dp[i] == bits count of num i
        '''
        dp = []
        
        for i in range(0, num+1):
            if i == 0:
                dp.append(0)
            elif i == 1:
                dp.append(1)
            else:
                '''
                  power of 2's bits count allways 1
                '''
                if i == 2*power:
                    dp.append(1)
                    power *= 2
                else:
                    '''
                       i.e. 15 = 0x1111 bits == 4
                             7 = 0x0111 bits == 3
                             8 = 0x1000 bits == 1

                             bits of 7 + 1 == bits of 15
                    '''
                    dp.append( dp[i-power]+1 )

        return dp

class unittest_countBits(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        inp = 2
        expected = [0,1,1]
        self.assertEqual(expected, self.sol.countBits(inp))

    def test_sample2(self):
        inp = 5
        expected = [0,1,1,2,1,2]
        self.assertEqual(expected, self.sol.countBits(inp))

    def test_sample3(self):
        inp = 16 
        expected = [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1]
        self.assertEqual(expected, self.sol.countBits(inp))

if __name__ == '__main__':
    unittest.main()
