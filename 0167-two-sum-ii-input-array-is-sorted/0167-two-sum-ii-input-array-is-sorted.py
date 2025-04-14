class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i]+ numbers[j]==target:
        #             return [i+1, j+1]. # time O(n^2), space: O(n)
# two pointers
        l,r=0,len(numbers)-1
        while l<r:
            cursum=numbers[l]+numbers[r]
            if cursum==target:
                return [l+1, r+1]
            elif cursum<target:
                l+=1
            elif cursum> target:
                r-=1
        

# time: O(n)
# space: O(1)
       





        