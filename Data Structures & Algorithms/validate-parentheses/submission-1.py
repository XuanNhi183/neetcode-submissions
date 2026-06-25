# {[()]}

class Solution:
    def isValid(self, s: str) -> bool:
        pairs={
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack=[]
        for c in s:
            if c not in pairs: 
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] != pairs[c]:
                    return False
                else:
                    stack.pop()
        return True if not stack else False
            


            
            