class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # hash= set(nums)
        # res=[]
        # for i in range(1, len(nums)+1):
        #     if i not in hash:
        #         res.append(i)
        # return res

        for n in nums:
            i= abs(n)-1
            nums[i]= -1 * abs(nums[i])

        res=[]
        for i, n in enumerate(nums):
            if n>0:
                res.append(i+1)
        return res


        