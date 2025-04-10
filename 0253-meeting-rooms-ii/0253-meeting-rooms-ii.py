class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # intervals.sort(key= lambda x: x[0])
        # print(intervals)
        # count=1

        # for i in range(len(intervals)-1):
        #     if intervals[i+1][0] < intervals[i][1]:
        #         count+=1
        #     else:
        #         continue
        # return count
        free=[]
        intervals.sort(key= lambda x: x[0])
        #push the first one
        heapq.heappush(free, intervals[0][1])

        for i in intervals[1:]:
            if free[0] <= i[0]:
                heapq.heappop(free)

            heapq.heappush(free, i[1])
        return len(free)


    



        