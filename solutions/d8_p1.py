from pathlib import Path
from collections import defaultdict

class day_8_p1():
    def __init__(self, input: Path, pad=0):
        with open(input) as f:
            self.input = [line.strip() for line in f.readlines()]
        
        # Create padding rows
        padding_row = '.' * (len(self.input[0]) + 2 * pad)  # Padding for left and right
        self.input = [padding_row] * pad + ['.' * pad + line + '.' * pad for line in self.input] + [padding_row] * pad
    
    def solve(self, input = None):
        if input is None:
            input = self.input
        antenna = defaultdict(list)
        for row,line in enumerate(input):
            for col,char in enumerate(line):
                if char != ".":
                    antenna[char].append((row,col))
        

        # antenna stores atenna types and locations
        # we need antinodes for each frequency:
        antinodes = set()
        for key in  antenna:
            new_antinodes = self.get_antinodes(antenna[key])
            for i in new_antinodes:
                if (0 <= i[0] < len(input)) and (0 <= i[1] < len(input[0])):
                    #only adds unique locations 
                    antinodes.add(i)
        return len(antinodes)
    
    
    def get_antinodes(self, locations) -> list:
        ants = set()
        for i in locations:
            for j in locations:
                if i != j:
                    diff = tuple(a-b for a,b in zip(i,j))
                    first_antinode = tuple(a-(2*b) for a,b in zip(i,diff))
                    second_antinode = tuple(a+(2*b) for a,b in zip(j,diff))
                    ants.add(first_antinode)
                    ants.add(second_antinode)
        return list(ants)
    

        






x = day_8_p1("inputs/day_8.txt",pad = 0)
p1 = x.solve()
print(p1)