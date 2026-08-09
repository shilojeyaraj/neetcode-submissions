class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        total = 0
        candSorted = sorted(candidates)
        def backtrack(i,curr, total):
            if total == target: #duplicate check: 
                res.append(curr.copy())
                return
            for j in range(i, len(candSorted)):
                if j > i and candSorted[j] == candSorted[j-1]:
                    continue 
                if total + candSorted[j] > target:
                    break
            
                curr.append(candSorted[j])
                backtrack(j+1,curr,total + candSorted[j])
                curr.pop()

        backtrack(0,[],0)
        return res