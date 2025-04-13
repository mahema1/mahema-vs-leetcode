class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap=defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]]+=1
        n= len(nums)//2
        for i in hashmap:
            if hashmap[i]> n:
                return i