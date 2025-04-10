class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])

    # Step 2: Check for overlap
        for i in range(len(intervals) - 1):
        # If next meeting starts before current one ends, overlap
            if intervals[i+1][0] < intervals[i][1]:
                return False

        return True
        