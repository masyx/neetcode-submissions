class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return None
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                val_2 = stack.pop()
                val_1 = stack.pop()
                res = 0
                if token == "+":
                    res = val_1 + val_2
                elif token == "-":
                    res = val_1 - val_2
                elif token == "*":
                    res = val_1 * val_2
                elif token == "/":
                    res = int(val_1 / val_2)
                stack.append(res)
        return stack[0]