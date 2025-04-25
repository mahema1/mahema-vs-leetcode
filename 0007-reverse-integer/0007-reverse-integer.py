class Solution:
    def reverse(self, x: int) -> int:
        y= abs(x)

        new=0
        while y!=0:
            last= y%10
            new= new*10+ last
            y=y//10

        new = new if x > 0 else -new

        # Check 32-bit signed integer range
        if new < (-2**31) or new > (2**31 - 1):
            return 0

        return new



        


