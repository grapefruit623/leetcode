# -*- coding:utf-8 -*-
import time

class Solution(object):
    '''
        TLE
    '''
    def canPartition_recursive(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        l = len(nums)

        if s % 2 != 0:
            return False

        partialSum = s/2

        return self.helper(partialSum, 0, 0, nums, l)

    def helper(self, ps, currentSum, index, nums, l):
        if ps == currentSum:
            return True

        for i in range(index, l):
            currentSum += nums[i]
            isFindPartial = self.helper(ps, currentSum, i+1, nums, l)

            if isFindPartial:
                return True
            currentSum -= nums[i]

        return False

    def canPartition(self, nums):
        """
        :type nums List[int]
        :rtype: bool
        """

        if sum(nums) % 2 != 0 or len(nums) == 1:
            return False

        self.halfSum = int(sum(nums)/2)

        self.dpResult = []

        for i in range(len(nums)+1):
            self.dpResult.append([])
            for j in range(self.halfSum+1):
                self.dpResult[i].append(0)

        return self.knapsack(nums)

    '''
        AC
        Trying to using 0/1 knapsack progorm's concept
    '''
    def knapsack(self, nums):
        for i in range(0, len(nums)):
            row = i+1
            for value in range(self.halfSum+1):
                if ( value >= nums[i] ):
                    self.dpResult[row][value] = max(self.dpResult[row-1][value],
                                            self.dpResult[row-1][value-nums[i]]+nums[i])
                else:
                    self.dpResult[row][value] = self.dpResult[row-1][value]

            if self.dpResult[row][value] == self.halfSum:
                return True

        return False
    """
        TLE
    """
    def bruteForce(self, nums):
        nums.sort()
        ans = sum(nums)
        if ans % 2 != 0:
            return False

        ans /= 2

        partial = []

        partial.append([])
        partial[0].append(0)
        partial[0].append(nums[0])

        for i in range(1, len(nums)):
            partial.append([])
            partial[i].append(0)
            partial[i].append(nums[i])

            for prev in partial[i-1]:
                if prev not in partial[i]:
                    partial[i].append(prev)
                if prev + nums[i] not in partial[i]:
                    partial[i].append(prev+nums[i])
            
            if ans in partial[i]:
                print (nums[i])
                return True
            
        return False


if __name__ == '__main__':
    sol = Solution()
    #data = [1,1]
    #data = [1,2,5]
    #data = [1, 5, 11, 5]
    #data = [1,1,2,2]
    """
        WA data
    """
    data = [19,33,38,60,81,49,13,61,50,73,60,82,73,29,65,62,53,29,53,86,16,83,52,67,41,53,18,48,32,35,51,72,22,22,76,97,68,88,64,19,76,66,45,29,95,24,95,29,95,76,65,35,24,85,95,87,64,97,75,88,88,65,43,79,6,5,70,51,73,87,76,68,56,57,69,77,22,27,29,12,55,58,18,30,66,53,53,81,94,76,28,41,77,17,60,32,62,62,88,61]
    before = time.time()
    print ( sol.canPartition(data) )
    print ( time.time() - before)
