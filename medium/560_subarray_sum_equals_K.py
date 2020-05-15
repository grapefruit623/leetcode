# -*- coding: utf-8 -*-
#! /usr/bin/python3
import unittest
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        hashTable = dict()
        s = 0

        for n in nums:
            s += n

            if s == k:
                ans += 1

            ans += hashTable.get(s-k, 0)
            hashTable.setdefault(s, 0)
            hashTable[s] += 1

        return ans

if __name__ == '__main__':
    unittest.main()

