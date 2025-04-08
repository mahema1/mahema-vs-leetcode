class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # # time:O(n), Space: O(n)
        # seen= set()

        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         return nums[i]
        #     else:
        #         seen.add(nums[i])

        # #time: O(n), space: O(1)
        # for num in nums:
        #     idx= abs(num)-1
        #     if nums[idx] < 0:
        #         return abs(num)
        #     nums[idx]*=-1
        # return -1





















        for num in nums:
            idx= abs(num)
            if nums[idx] < 0:
                return idx
            nums[idx]*=-1
        return -1
        