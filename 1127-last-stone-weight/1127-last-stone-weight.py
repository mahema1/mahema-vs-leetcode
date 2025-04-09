class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]= - stones[i]
        heapq.heapify(stones) # made the heap --- max heap

        while len(stones)>1:
            v1= -(heapq.heappop(stones))
            v2= -(heapq.heappop(stones))

            if v1!=v2:
                heapq.heappush(stones, -(v1-v2))

        return -stones[0] if stones else 0



            
            



        