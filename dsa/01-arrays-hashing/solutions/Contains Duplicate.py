class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = {}
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s[nums[i]]=1    
        return False
        