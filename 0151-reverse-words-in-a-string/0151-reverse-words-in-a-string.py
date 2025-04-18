class Solution:
    def reverseWords(self, s: str) -> str:
        # # we can use a stack -O(n)space, else two pointers.
        # words= s.split()
        # l,r=0, len(words)-1
        # while l<r:
        #     words[l], words[r]= words[r], words[l]
        #     l+=1
        #     r-=1
        # return " ".join(words)

        ## time: O(n), space: O(1)

        words= s.split()
        stack=[]
        res=[]
        for word in words:
            stack.append(word)
            
        while stack:
            res.append(stack.pop())
        return " ".join(res)
        
        
        
        