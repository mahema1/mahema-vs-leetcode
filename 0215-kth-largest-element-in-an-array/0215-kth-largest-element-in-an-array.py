import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # #heapq- min heap 
        # for i in range(len(nums)):
        #     nums[i]=-nums[i]
        # heapq.heapify(nums)

        # for x in range(k-1):
        #     heapq.heappop(nums)
        # return -heapq.heappop(nums)

        minHeap=[]
        for i in nums:
            heapq.heappush(minHeap, i)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return  minHeap[0]
        