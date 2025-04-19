class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for char in s:
            if char!="]":
                stack.append(char)
            else:
                sub=""
                while stack and stack[-1] !='[':
                    sub= stack.pop()+sub # popping the elements till we find the open bracket
                stack.pop() # popping the open bracket

                num=""
                while stack and stack[-1].isdigit():
                    num= stack.pop()+num
                stack.append(int(num)*sub)
        return "".join(stack)
