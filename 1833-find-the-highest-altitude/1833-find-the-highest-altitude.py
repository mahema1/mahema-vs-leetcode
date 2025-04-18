class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix=0
        res=[]
        res.append(prefix)
        for g in gain:
            prefix+= g 
            res.append(prefix)
        return max(res)
        