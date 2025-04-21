class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # slow 1 banana per hour, worst max banana
        res = r

        while l <= r:
            mid = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / mid)
            if totalTime <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res