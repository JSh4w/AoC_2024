from pathlib import Path
from collections import defaultdict
import sys 
sys.set_int_max_str_digits(22000)  # Set to a higher limit, e.g., 20000

class day_9_p1():
    def __init__(self, input: Path, pad=0):
        with open(input) as f:
            self.input = [line.strip() for line in f.readlines()]
        
        # Create padding rows
        padding_row = '.' * (len(self.input[0]) + 2 * pad)  # Padding for left and right
        self.input = [padding_row] * pad + ['.' * pad + line + '.' * pad for line in self.input] + [padding_row] * pad
    
    def solve(self, input=None):
        if input is None:
            input = self.input
            input = input[0]

        numbers = []
        index = 0 
        end_pointer = len(input) -1
        end_pointer_value = int(input[end_pointer])
        while index < end_pointer:
            input_value = int(input[index])
            if index % 2 == 0:
                for _ in range(input_value):
                    #index +1 each time so take halfs 
                    numbers.append(index//2)
            #empty blocks so need to use from the back
            else:
                for _ in range(input_value):
                    if end_pointer_value < 1:
                        end_pointer -= 2
                        end_pointer_value = int(input[end_pointer])
                    
                    if end_pointer > index:
                        end_pointer_value -= 1
                        numbers.append(end_pointer//2)
            index +=1
        
        if end_pointer >= index and end_pointer_value > 0:
            for _ in range(end_pointer_value):
                numbers.append(end_pointer//2)
        
        return sum(idx * val for idx, val in enumerate(numbers) if val)

                        




        return total_sum

x = day_9_p1("inputs/d9.txt",pad = 0)
ex ="2333133121414131402"
p1 = x.solve()
print(p1)