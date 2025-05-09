class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #set for  subring - if we get duplicates
        #time : O(n)
        #space: O(n)

        res=0
        charset= set()
        l=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res= max(res, r-l+1)
        return res

