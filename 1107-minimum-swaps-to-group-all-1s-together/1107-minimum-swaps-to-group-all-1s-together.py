class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones= sum(data)
        if ones==len(data) or len(data)==1:
            return 0
        cur_ones= max_ones= sum(data[:ones])
        for i in range(ones, len(data)):
            cur_ones+=data[i]- data[i-ones]
            max_ones= max(max_ones, cur_ones)
        return ones- max_ones