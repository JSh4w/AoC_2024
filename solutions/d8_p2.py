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
        len_ant = len(antenna)
        idx =0 
        print("starting")
        for key in  antenna:
            new_antinodes = self.get_antinodes(antenna[key], len(input), len(input[0]))
            for i in new_antinodes:
                if (0 <= i[0] < len(input)) and (0 <= i[1] < len(input[0])):
                    #only adds unique locations 
                    antinodes.add(i)#
                    idx += 1
                    print(f"{idx} out of {len_ant}")
        return len(antinodes)
    
    
    def get_antinodes(self, locations, rows,cols) -> list:
        ants = set()
        for i in locations:
            for j in locations:
                if i != j:
                    larg_diff = tuple(a-b for a,b in zip(i,j))
                    diff = self.smallest_ratio(larg_diff)
                    x,y = i 
                    while (0 <= x < rows) and (0 <= y < cols):
                        first_antinode = tuple(a-b for a,b in zip((x,y),diff))
                        ants.add(first_antinode)
                        x, y = first_antinode
                    x,y = i
                    while (0 <= x <= rows) and (0 <= y <= cols):
                        second_antinode = tuple(a+b for a,b in zip((x,y),diff))
                        ants.add(second_antinode)
                        x, y = second_antinode
        return list(ants)


    def smallest_ratio(self,tup : tuple):
        a = tup[0]
        b= tup[1]
        #gcd euclidean algorithm
        while b:
            a, b = b, a % b
        gcd = a  
        # using int incased of floating point rounding erors
        return (int(tup[0]/gcd), int(tup[1]/gcd))
    

        






x = day_8_p1("inputs/day_8.txt",pad = 0)
p1 = x.solve()
print(p1)