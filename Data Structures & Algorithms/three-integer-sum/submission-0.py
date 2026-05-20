class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsnew = sorted(nums)
        seen = set()
        result = []
        left = 1
        right = len(numsnew) - 1
        for i in range(len(numsnew)):
            if i > 0 and numsnew[i] == numsnew[i-1]: 
                continue
            left = i+1
            right = len(numsnew) - 1
            while left < right: 
                value = numsnew[i] + numsnew[left] + numsnew[right]
                if value > 0: 
                    right -= 1
                if value < 0:
                    left += 1
                if value == 0:

                    result.append([numsnew[i],numsnew[left],numsnew[right]])
                    while left < right and numsnew[left] == numsnew[left+1]: 
                        left += 1
                    while left < right and numsnew[right] == numsnew[right-1]: 
                        right -= 1
                    left += 1
                    right -= 1
        return result