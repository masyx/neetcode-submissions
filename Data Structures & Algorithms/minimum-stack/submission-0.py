class MinStack:
    def __init__(self):
        self.values = []
        # [[1,1], [0, 1]]
        self.min_values = []
        
    def push(self, val: int) -> None:
        self.values.append(val)
        if not self.min_values or val < self.min_values[-1][0]:
            self.min_values.append([val, 1])
        elif val == self.min_values[-1][0]:
            self.min_values[-1][1] += 1
    
    def pop(self) -> None:
        if self.values:
            val = self.values.pop()
            if val == self.min_values[-1][0]:
                self.min_values[-1][1] -= 1
                if self.min_values[-1][1] == 0:
                    self.min_values.pop()
    
    def top(self) -> int:
        if self.values:
            return self.values[-1]
    
    def getMin(self) -> int:
        if self.min_values:
            return self.min_values[-1][0]