class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for a in asteroids:
            while stack and a<0 and stack[-1]>0:
                if abs(a) > stack[-1]: # curretn left moving is larger, right explodes
                    stack.pop()

                elif stack[-1] > abs(a):
                    a=0
                else:
                    
                    stack.pop()
                    a=0
            if a:
                stack.append(a)
        return stack
            
        