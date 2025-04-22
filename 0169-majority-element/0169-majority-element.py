class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap=defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]]+=1
        n= len(nums)//2
        # for num in hashmap:
        #     if hashmap[num] > n:
        #         return num
        for key, val in hashmap.items():
            if val>n:
                return key

        # nums.sort()
        # return nums[len(nums)//2]
        