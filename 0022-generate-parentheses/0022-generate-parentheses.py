class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open< n
        # only add a  closing parenthesis if closed < open 
        # valid iff open== close==n
        stack=[]
        res=[]
        def dfs(openn, closen):
            if openn== closen== n:
                res.append("".join(stack))
                return 

            if openn<n:
                stack.append("(")
                dfs(openn+1, closen)
                stack.pop()

            if closen<openn:
                stack.append(")")
                dfs(openn, closen+1)
                stack.pop()
        dfs(0,0)
        return res