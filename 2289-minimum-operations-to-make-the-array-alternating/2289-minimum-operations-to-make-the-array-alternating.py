class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        even = nums[::2]
        odd = nums[1::2]

        even_count = Counter(even).most_common(2)
        odd_count = Counter(odd).most_common(2)

        # Fill in dummy values if we don't have 2 most common
        even_count += [(None, 0)] * (2 - len(even_count))
        odd_count += [(None, 0)] * (2 - len(odd_count))

        # Case 1: most frequent in even != most in odd → valid
        if even_count[0][0] != odd_count[0][0]:
            return (len(even) - even_count[0][1]) + (len(odd) - odd_count[0][1])
        else:
            # Try two options:
            # 1. Use even[0], odd[1]
            op1 = (len(even) - even_count[0][1]) + (len(odd) - odd_count[1][1])
            # 2. Use even[1], odd[0]
            op2 = (len(even) - even_count[1][1]) + (len(odd) - odd_count[0][1])
            return min(op1, op2)
