class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap= Counter(arr)
        seen= set()
        for i in hashmap.values():
            if i in seen:
                return False
            seen.add(i)
        return True


        