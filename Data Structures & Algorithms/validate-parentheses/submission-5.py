class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = [s[0]]
        map = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        for i in range(1, len(s)):
            if s[i] in map.values():
                stack.append(s[i])
        
            else:
                if not stack or stack[-1] != map[s[i]]:
                    return False
                stack.pop()
                
        return len(stack) == 0


        