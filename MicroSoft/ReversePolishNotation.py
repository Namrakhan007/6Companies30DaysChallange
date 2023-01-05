class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "*+-/"
    
        for opp in tokens:
            if opp in ops:
                a = stack.pop()
                b = stack.pop()
                if opp == "+":
                    stack.append(a+b)
                elif opp =="-":
                    stack.append(b-a)
                elif opp == "*":
                    stack.append(a*b)
                elif opp == "/":
                    stack.append(int(b/a))
                
                    
            else:
                stack.append(int(opp))
        return stack.pop()
