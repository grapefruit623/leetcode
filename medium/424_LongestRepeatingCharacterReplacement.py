# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest
import string

class Solution:
    '''
        AC
    '''
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= k:
            return len(s)

        start = end = 0
        ans = -1
        alphabetCount = {}
        maxAlphabetCount = -1
        for a in string.ascii_uppercase:
            alphabetCount[a] = 0

        while start<len(s) and end<len(s):
            slidingWindowsLen = end-start+1
            alphabetCount[s[end]] += 1
            maxAlphabetCount = max(maxAlphabetCount, alphabetCount[s[end]])

            '''
                Which means can modify <= k's alphabets to become the most alphabet in
                current sliding window.
            '''
            if slidingWindowsLen - maxAlphabetCount <= k:
                ans = max(ans, slidingWindowsLen)
            else:
                '''
                    >k means that I need to modify > k alphabets in current range of sliding window
                    to get a continue substring, but that is impossible. 
                    Moving sliding window to try to get valid substring.
                '''
                alphabetCount[s[start]] -= 1
                start += 1
            end += 1

        return ans        

class unittest_characterReplacement(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sample1(self):
        s = "ABAB"
        k = 2
        self.assertEqual(self.sol.characterReplacement(s,k), 4)

    def test_sample2(self):
        s = "AABABBA"
        k = 1
        self.assertEqual(self.sol.characterReplacement(s,k), 4)

    def test_sample3(self):
        s = "ABCD"
        k = 5
        self.assertEqual(self.sol.characterReplacement(s,k), 4)

if __name__ == "__main__":
    unittest.main()
