# ab
# acba
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_1 = {}
        for char in s1:
            counter_1[char] = counter_1.get(char, 0) + 1
        
        l = 0
        counter_2 = {}
        for r in range(len(s2)):
            counter_2[s2[r]] = counter_2.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                counter_2[s2[l]] -= 1
                if counter_2[s2[l]] == 0:
                    del counter_2[s2[l]]
                l += 1
            if counter_1 == counter_2:
                return True
        return False