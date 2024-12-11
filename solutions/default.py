from pathlib import Path
from collections import defaultdict

class day_X_p1():
    def __init__(self, input: Path, pad=0):
        with open(input) as f:
            self.input = [line.strip() for line in f.readlines()]
        
        # Create padding rows
        padding_row = '.' * (len(self.input[0]) + 2 * pad)  # Padding for left and right
        self.input = [padding_row] * pad + ['.' * pad + line + '.' * pad for line in self.input] + [padding_row] * pad
    
    def solve(self, input = None):
        if input is None:
            input = self.input
        ans = 0
        return ans 

x = day_X_p1("inputs/day_8.txt",pad = 0)
p1 = x.solve()
print(p1)