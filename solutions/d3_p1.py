import re
with open("day_3.txt") as file:
    text = file.read().strip()

    sum = 0
    reg = r"mul\((\d{1,3}),(\d{1,3})\)"
    for i in range(len(text)):
        instr = re.match(reg, text[i:])
        if instr is not None:
            x,y = int(instr.group(1)), int(instr.group(2))
            sum+= x*y
print(sum)