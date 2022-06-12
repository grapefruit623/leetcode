class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        middle=-1
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        while end > start:
            middle=int(math.ceil(end+start)/2)
            
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end=middle
            else:
                start=middle
            
            if start == end-1:
                if nums[start] == target:
                    return start
                elif nums[end] == target:
                    return end
                else:
                    return -1
            
        return -1
