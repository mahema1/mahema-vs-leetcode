class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # brute force: time: O(n), space: O(n)
        # res=[]
        # l,r= 0,0
        # while l<len(nums1) and  r< len(nums2):
        #     if nums1[l] <= nums2[r]:
        #         res.append(nums1[l])
        #         l+=1
        #     else:
        #         res.append(nums2[r])
        #         r+=1
        # while l< len(nums1):
        #     res.append(nums1[l])
        #     l+=1
        # while r< len(nums2):
        #     res.append(nums2[r])
        #     r+=1
        # return res

        last= m+n-1
        while m>0 and n>0:
            if nums1[m-1]> nums2[n-1]:
                nums1[last]= nums1[m-1]
                m-=1
            else:
                nums1[last]= nums2[n-1]
                n-=1
            last-=1
        # if there are elements left in nums1, no problem they are already in sorted array
        #if there are elements left ijn nums2, we need to add them.
        while n>0:
            nums1[last]= nums2[n-1]
            n-=1
            last-=1
        
        