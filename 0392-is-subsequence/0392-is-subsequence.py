class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i,j=0,0
        while i< len(t) and j<len(s):
            if s[j]!= t[i]:
                i+=1
            else:
                j+=1
                i+=1
            if j== len(s):
                return True
        return False
        