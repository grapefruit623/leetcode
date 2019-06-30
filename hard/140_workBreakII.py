# -*- coding:utf-8 -*-
import unittest
from typing import List

class Solution:
    
    '''
        TLE 
        This solution is created by 139 wordBreakI's algorithm
    '''
    def wordBreak(self, s: str, wordDict: List[str])->bool:
        strLen = len(s)
        dp = [False]*(strLen+1)
        dp[0] = True

        ans = []
        for i in range(strLen+1):
            ans.append( [] )


        for i in range(1, strLen+1):
            for j in range(i, strLen+1):
                if s[i-1:j] in wordDict:
                    if dp[i-1] == True:
                        dp[j] = True

                        if ans[i-1] == []:
                            ans[j].append([s[i-1:j]])
                        else:
                            for a in ans[i-1]:
                                ans[j].append( a + [ s[i-1:j] ])
        ret = []
        for a in ans[-1]:
            ret.append( " ".join(a) )

        return ret

class unittest_wordBreak(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    '''
    def test_sample2(self):
        s = "applepenapple"
        wordDict = {"apple", "pen"}
        expected = True
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))

    def test_special(self):
        s = 'abc'
        wordDict = ['a', 'b', 'bc']
        expected = True
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))

    def test_sample1(self):
        s = "leetcode"
        wordDict = {"leet", "code"}
        expected = True
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))
   ''' 

    '''
    def test_special(self):
        s = 'a'
        wordDict = ['a']
        expected = ["a"]
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))
    '''

    '''
    def test_sample3(self):
        s = "catsanddog"
        wordDict = {"cats", "sand", "and", "cat", "dog"}
        expected = [ "cat sand dog", "cats and dog" ]
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))
    '''
    def test_sampleTLE(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        expected = []
        self.assertEqual(expected, self.sol.wordBreak(s, wordDict))

if __name__ == '__main__':
    unittest.main()
