class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # #max heap
        # for i in range(len(nums)):
        #     nums[i]= -nums[i]
        # heapq.heapify(nums)
        # while (k-1):
        #     heapq.heappop(nums)
        #     k-=1
        # return - nums[0]

        #min heap
        minHeap=[]
        for i in nums:
            heapq.heappush(minHeap,i)
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        return minHeap[0]



    
        