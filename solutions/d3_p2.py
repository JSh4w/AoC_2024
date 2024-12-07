import re
with open("day_3.txt") as file:
    text = file.read().strip()

    sum = 0
    reg = r"mul\((\d{1,3}),(\d{1,3})\)"
    en = True
    for i in range(len(text)):
        instr = re.match(reg, text[i:])
        if text[i:].startswith("do()"):
            en = True
        if text[i:].startswith("don't()"):
            en = False
        if instr is not None:
            x,y = int(instr.group(1)), int(instr.group(2))
            if en:
                sum += x * y
print(sum)