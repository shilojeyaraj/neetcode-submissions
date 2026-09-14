class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        total = tokens[0]
        for i in tokens:
            if i in ops:
                b = stack.pop()
                a = stack.pop()
                
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a * b)
                else: 
                    stack.append(int(a / b))
            else:
                stack.append(int(i))
        
        return stack[-1]


                

                

        