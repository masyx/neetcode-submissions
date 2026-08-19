class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}/:{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            delim_index = s.find("/:", i)
            length = int(s[i: delim_index])
            result.append(s[delim_index + 2: delim_index + 2 + length])
            i = delim_index + 2 + length
        return result
