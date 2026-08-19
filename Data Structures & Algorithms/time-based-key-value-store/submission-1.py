from collections import defaultdict 

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])
    #i  0  1  2  3
    #  13 20 26 50
    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        if not values:
            return ""

        l = 0
        r = len(values) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            stored_timestamp, value = values[mid]

            if stored_timestamp <= timestamp:
                res = value
                l = mid + 1
            else:
                r = mid - 1

        return res
        
