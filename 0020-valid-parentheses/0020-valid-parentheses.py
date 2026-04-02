class Solution:
    def isValid(self, s: str) -> bool:
        # }
        stack=[]
        mapping={
            '}':'{',
            ']':'[',
            ')':'('
        }
        for ch in s:
            if ch in '{([': #opening brackets
                stack.append(ch)
            else: #closing brackets
                pair = mapping[ch] 
                if len(stack)!=0:#stack is not empty
                    if pair!=stack[-1]:
                        return False
                    else:
                        stack.pop()
                else:#stack is empty
                    return False
                
        if len(stack)==0:
            return True
        else:
            return False