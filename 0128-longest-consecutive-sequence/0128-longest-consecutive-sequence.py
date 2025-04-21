class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we will find the sequences, by looking for (n-1)th element in the set,
        # if it exists then it doesnt start, if it doesn't exist then it is the start
        numSet=set(nums) # constact look ups
        longest=0
        for n in numSet:
            if (n-1) not in numSet: # start of the seqence
                length=1
                current= n+1
                while current in numSet:
                    length+=1
                    current+=1
                longest= max(longest, length)
        return longest
                
    #         *1,2,3,4         *100*         *200*
    # --------------------------------------------- number line

        