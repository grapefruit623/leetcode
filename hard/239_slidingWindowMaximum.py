#! /usr/bin/python3
# -*- coding: utf-8 -*-

class Solution(object):
    """
        AC
        But is that O(n^2) complexity?
    """
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0 or k < 1:
            return []

        ans = []
        totalStep = len(nums) - k
        nums = list(enumerate(nums))

        currentMax = max(nums[0:k], key=lambda x:x[1])
        ans.append(currentMax[1])

        for i in xrange(totalStep):
            shiftPos = i+k
            pos = nums[shiftPos][0]
            value = nums[shiftPos][1]

            if pos - currentMax[0] == k:
                currentMax = max(nums[ currentMax[0]+1:shiftPos+1], key=lambda x:x[1])
                ans.append(currentMax[1])
            else:
                if value > currentMax[1]:
                    ans.append(value)
                    currentMax = (pos, value)
                else:
                    ans.append(currentMax[1])
        return ans

if __name__ == '__main__':
    '''
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    '''
    nums = [-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7]
    k = 7

    sol = Solution()
    print (sol.maxSlidingWindow(nums, k))
