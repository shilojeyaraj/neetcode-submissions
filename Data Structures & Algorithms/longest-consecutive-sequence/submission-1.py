class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = set(nums)
        res = 0
        for num in nums:
            streak,curr = 0,num
            while curr in table: 
                streak += 1
                curr += 1
            res = max(res, streak)
        return res
        
        