class Solution:
    def reverseVowels(self, s: str) -> str:
        s= list(s)
        l, r=0, len(s)-1
        vowels={"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        while l<r:
            if s[l] not in vowels:
                l+=1
            elif s[r] not in vowels:
                r-=1
            else:
                s[l], s[r]= s[r], s[l]
                l+=1
                r-=1
        return "".join(s)

            
