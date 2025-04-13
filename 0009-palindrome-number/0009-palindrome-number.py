class Solution:
    def isPalindrome(self, x: int) -> bool:

        # #converted into string
        # s= str(x)
        # l,r= 0, len(s)-1
        # while l<=r:
        #     if s[l]==s[r]:
        #         l+=1
        #         r-=1
        #     else:
        #         return False
        # return True

        if x<0:
            return False
        div=1
        while x> 10*div:
            div*=10
        while x:
            right= x%10
            left= x//div
            if right!= left: return False

            x= (x%div)//10
            div= div/100
        return True

        



        
        