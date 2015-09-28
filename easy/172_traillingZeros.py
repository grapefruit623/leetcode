#! /usr/bin/python3
# -*- coding: utf-8 -*-

'''
    refer: https://en.wikipedia.org/wiki/Trailing_zero
'''


class Solution(object):
    '''
        n!'s trailing zeros
    '''
    def trailingZeroes(self, n):
        ans = 0
        k = 0
        while 5**(k+1) <= n:
            k += 1

        for i in range(k, 0, -1):
            ans += n/(5**i)

        return ans

if __name__ == '__main__':
    s = Solution()
    print s.trailingZeros(32)
