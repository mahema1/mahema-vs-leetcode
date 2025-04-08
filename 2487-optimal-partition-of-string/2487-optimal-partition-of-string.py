class Solution:
    def partitionString(self, s: str) -> int:
        seen= set()
        temp=""
        count=0

        for char in s:
            if char in seen:
                seen.clear()
                count+=1
                temp=""
            seen.add(char)
            temp+=char
        if seen:
            count+=1
            
        return count

            


        