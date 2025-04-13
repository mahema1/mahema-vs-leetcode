class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        i, j=0,0
        if not word1:
            return word2
        if not word2:
            return word1
        
        while i< len(word1) and j<len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        res.append(word1[i:])
        res.append(word2[j:])

        return ("".join(res))
        # res=[]
        # if not word1:
        #     return word2
        # if not word2:
        #     return word1
        
        # for i in range(min(len(word1), len(word2))):
        #     res.append(word1[i])
        #     res.append(word2[i])
        
        # if len(word1)> len(word2):
        #     for ch in word1[len(word2):]:
        #         res.append(ch)
        # if len(word2)> len(word1):
        #     for ch in word2[len(word1):]:
        #         res.append(ch)
        

        # return ("".join(res))



        