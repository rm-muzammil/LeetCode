class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        possible = 0
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target:
                return i
            else:
                possible +=1
        return possible
            
            
        