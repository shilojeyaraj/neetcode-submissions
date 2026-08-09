class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sum = 0
        path = []
        def backtrack (i, path, sum):
            if sum == target: 
                res.append(path.copy())
                return
            
            
            if sum >= target or i >= len(nums):
                return
            path.append(nums[i])
            
            backtrack(i,path,sum + nums[i])
            path.pop()
            backtrack(i+1,path,sum)

        backtrack(0,[],0)
        return res