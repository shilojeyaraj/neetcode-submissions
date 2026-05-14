class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        bigRes = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                bigRes *= num
            else: 
                zero_count += 1
        result = []
        
        for i in nums:
            if zero_count > 1:
                result.append(0)           # more than one zero → all zeros
            elif zero_count == 1:
                if i == 0:
                    result.append(bigRes)  # only the zero position gets product
                else:
                    result.append(0) 
            else: 
                result.append(bigRes // i)
        return result