class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2, 7, 11, 15 traget=9 
        # 9-2==7
        # 9-7== 2
        # 9-11==-2
        # 9-15==-6

        # {2:0, 7:1, 11:2, 15:3}
        hashmap={} 
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        print(hashmap)

        for x in range(len(nums)):
            y= target-nums[x]
            if y in hashmap and hashmap[y]!= x: # no duplicates
                return [x, hashmap[y]]

        # hashmap = {}
        # for i in range(len(nums)):
        #     hashmap[target - nums[i]] = i

        # for i in range(len(nums)):
        #     if nums[i] in hashmap and hashmap[nums[i]] != i:
        #         return [i, hashmap[nums[i]]]
        

                #time: O(n) space: O(n)

       
