class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for num in range(0,len(nums)-1):
            for i in range(num+1,len(nums)):
                if nums[i]==nums[num]: return True
            return False