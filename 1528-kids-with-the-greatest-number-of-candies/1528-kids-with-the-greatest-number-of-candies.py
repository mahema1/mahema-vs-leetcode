class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum= max(candies)
        print(maximum)
        res=[]
        for i in range(len(candies)):
            if candies[i]+ extraCandies >= maximum:
                res.append(True)
            else:
                res.append(False)

        return res
        