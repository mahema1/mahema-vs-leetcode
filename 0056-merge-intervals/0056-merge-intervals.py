class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        if not intervals:
            return None
        output=[intervals[0]]# help in comparing the next ones
        

        for start, end in intervals[1:]:
            lastEnd=output[-1][1] # end time of the last interval

            if start <= lastEnd:
                '''if we had [1,5][2,4] we need to take the max'''
                output[-1][1]= max(lastEnd, end)
            else:
                output.append([start, end])
        return output



        #     if intervals[i+1][0] <= intervals[i][1]:
        #         new.append([intervals[i][0], max(intervals[i+1][1], intervals[i][1])])
        #     else:
        #         new.append(intervals[i+1])
            
        # return new

        