class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        count2 = Counter()
        l = 0
        for r in range(len(s2)):
            count2[s2[r]] += 1
            if r - l + 1 > len(s1):
                if count2[s2[l]] == 1:
                    del count2[s2[l]]
                else:
                    count2[s2[l]] -= 1
                l += 1
            if count1 == count2:
                return True
        return False