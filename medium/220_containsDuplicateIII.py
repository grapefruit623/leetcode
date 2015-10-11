#! /usr/bin/python3
# -*- coding: utf-8 -*-
import math
import time

__author__ = "grapefruit623"

class Solution(object):
    '''
        Time limited exceeded!
    '''
    def containsNearbyAlmostDuplicate(self, nums, k, t):

        if k <= 0 or t < 0 or len(nums) == 1:
            return False

        maxNum = max(nums)
        bucket = {}        

        for i, v in enumerate(nums):
            '''
                Bucket's index number is value slot
            '''
            shiftValue = int(math.ceil(v/(t+1)))

            '''
                Checking near bucket
            '''
            for key in [ shiftValue-1, shiftValue, shiftValue+1 ]:
                if key in bucket.keys():
                    for m in bucket[key]:
                        if abs(m[1]-v) <= t and abs(m[0]-i) <= k:
                            return True

            if shiftValue not in bucket.keys():
                bucket[shiftValue] = []

            bucket[shiftValue].append((i,v))


        return False

    '''
        AC
        I saw a probably solution keyword: 
            <---Bucket sort--->
            the bucket's size meaning is value diffence ???
            (all elements in same bucket are difference <= t ???)
            how can I do it? if no element in bucket dict ???
    '''
    def AC_containsNearbyAlmostDuplicate(self, nums, k, t):

        if k <= 0 or t < 0 or len(nums) == 1:
            return False

        maxNum = max(nums)
        bucket = {}        

        for i, v in enumerate(nums):
            '''
                Bucket's index number is value slot
            '''
            shiftValue = v/(t+1)

            '''
                Checking near bucket
            '''
            for key in [ shiftValue-1, shiftValue, shiftValue+1 ]:
                if key in bucket:
                    if abs(bucket[key][1]-v) <= t and abs(bucket[key][0]-i) <= k:
                        return True

            '''
            if shiftValue not in bucket.keys():
                bucket[shiftValue] = []
            '''
            '''
                Why can just a data?, not elements in same bucket???
            '''
            print (shiftValue, (i,v))
            bucket[shiftValue] = (i,v)

            if i > k:
                popKey = nums[(i-k)]/(t+1)
                if popKey in bucket:
                    bucket.pop( popKey )
            
            print (bucket)

        return False
if __name__ == '__main__':
    s = Solution()
    nums = []
    nums = [1, 0, 1, 1]
    t = 0
    k = 1

    '''
    with open('data.txt', 'r') as f:
        r = f.readlines()
        n = r[0]
        t = int(r[1])
        k = int(r[2])

        n = n[1:-2].split(',')  # big int list
        for i in n:
            nums.append(int(i))
    '''
    start = time.time()
    print (s.containsNearbyAlmostDuplicate(nums, t, k))
    end = time.time()
    print ( end - start )
