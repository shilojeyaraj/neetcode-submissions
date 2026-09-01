import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
         #use heap, pop anything thats not top k
       self.miniHeap = nums
       self.k = k
       heapq.heapify(self.miniHeap)
       while len(self.miniHeap) > k:
            heapq.heappop(self.miniHeap)
       
    def add(self, val: int) -> int:
        heapq.heappush(self.miniHeap,val)
        if len(self.miniHeap) > self.k:
            heapq.heappop(self.miniHeap)
        return self.miniHeap[0]
