ex = "0123\n1234\n8765\n9876"
ex = ex.split()
from pathlib import Path
from collections import defaultdict, deque
from typing import List, Tuple, Set

class day_10_p1():
    def __init__(self, input: Path, pad=0):
        with open(input) as f:
            self.input = [line.strip() for line in f.readlines()]
        
        # Create padding rows
        padding_row = '.' * (len(self.input[0]) + 2 * pad)  # Padding for left and right
        self.input = [padding_row] * pad + ['.' * pad + line + '.' * pad for line in self.input] + [padding_row] * pad
    
    def solve(self, input = None):
        if input is None:
            input = self.input
        self.rows = len(input)
        self.cols = len(input[0])
        self.dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        sum = 0
        for rx, r in enumerate(input):
            for cx, c in enumerate(r):
                if c == "0":
                    sum += len(self.breadth_search(rx,cx))

        return sum

    def breadth_search(self, start_row : int, start_col : int) -> Set[Tuple[int,int]]:
        nine_locations = set()

        def is_valid(row: int, col: int, expected_val : int) -> bool:
            if 0<= row < self.rows and 0 <= col < self.cols and int(self.input[row][col]) == expected_val:
                return True
            else:
                return False
            
        queue = deque([(start_row, start_col, 0)])
        visited = {(start_row, start_col)}

        while queue:
            curr_row, curr_col, curr_value = queue.popleft()
            if curr_value == 9:
                nine_locations.add((curr_row, curr_col))
                continue
                
            for dx, dy in self.dirs:
                next_row, next_col = curr_row + dy, curr_col + dx
                if (is_valid(next_row, next_col, curr_value +1) and
                    (next_row, next_col) not in visited):
                    queue.append((next_row,next_col, curr_value+1))
                    visited.add((next_row, next_col))
        return nine_locations


x = day_10_p1("inputs/d10.txt",pad = 0)
p1 = x.solve()
print(p1)