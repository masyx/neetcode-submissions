class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # ops = ["5","D","+","C"]
        # res = [5, 10]
        res = []
        for el in operations:
            if el == "+":
                res.append(res[-1] + res[-2])
            elif el == "C":
                res.pop()
            elif el == "D":
                res.append(2 * res[-1])
            else:
                res.append(int(el))
        return sum(res)