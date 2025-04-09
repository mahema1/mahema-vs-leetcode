class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count= Counter(nums)
        # print(count)

        # sorted_items= sorted(count.items(), key= lambda x: x[1], reverse= True)
        # res=[]
        # for i in range(k):
        #     key, val= sorted_items[i]
        #     res.append(key)
        # return res


        count= Counter(nums)
        heap=[]
        for key, val in count.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [key for (val, key) in heap]
        


        

