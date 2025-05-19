class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={")" : "(", "]": "[", "}":"{"}
        stack=[]
        for c in s:
            if c not in hashmap:
                stack.append(c)
            if c in hashmap:
                if not stack:
                    return False
                else:
                    char= stack.pop()
                
                if char!=hashmap[c]:
                    return False
                else:
                    continue
        return True if not stack else False

       
