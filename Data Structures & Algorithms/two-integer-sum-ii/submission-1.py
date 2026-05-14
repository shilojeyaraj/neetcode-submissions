class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        right = 0
        left = size - 1
        ans = []
        while right < left: 
            if numbers[right] + numbers[left] > target: 
                left -= 1
            if numbers[right] + numbers[left] < target: 
                right += 1
            if numbers[right] + numbers[left] == target:
                ans.append(right + 1)
                ans.append(left + 1)
                return ans
