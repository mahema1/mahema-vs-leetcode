class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        hashmap={"a", "e", "i", "o", "u"}
        curr=0
        for i in range(k):
            if s[i] in hashmap:
                curr+=1
        maxx=curr
        for i in range(k, len(s)):
            if s[i] in hashmap:
                curr+=1
            if s[i-k] in hashmap:
                curr-=1
            maxx= max(maxx, curr)
        return maxx

        