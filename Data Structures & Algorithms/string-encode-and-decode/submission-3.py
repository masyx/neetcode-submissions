class Solution:

    def encode(self, strs: List[str]) -> str:
        def return_count(s):
            count = str(len(s))
            zeros_needed = 3 - len(count)
            return "0" * zeros_needed + count

        res = ""
        for s in strs:
            res += return_count(s) + s
        return res
    # i = 3
    #0123456789101112
    #003cat004lo v e
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): 
            length = int(s[i : i + 3])
            word = s[i + 3: i + 3 + length]
            res.append(word)
            i += 3 + length
        return res