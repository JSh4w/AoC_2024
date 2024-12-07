f = open("day_6.txt") 
inp = f.readlines()
map = []
strt = [0,0]
for row, line in enumerate(inp):
    line = list(line)
    for idx , i in enumerate(line):
        if i == "^":
            strt = [row, idx]
            line[idx] = "."
    map.append("".join(line).strip())
dirs = {"U":(-1,0), "R":(0,1), "D":(1,0), "L":(0,-1)}
ROWS = (0, len(map) -1)
COLS = (0, len(map[0]) -1)
r,c = strt
dir  = "U"
unique = set()
while r in range(ROWS[0], ROWS[1] + 1) and c in range(COLS[0], COLS[1] + 1):  # Corrected boundary check
    move = dirs[dir]
    check = (r + move[0], c + move[1])
    
    # Check if the next position is within bounds
    if check[0] < ROWS[0] or check[0] > ROWS[1] or check[1] < COLS[0] or check[1] > COLS[1]:
        break  # Exit if out of bounds

    if map[check[0]][check[1]] == ".":
        r, c = check  # Move to the next position
        unique.add((r,c)) 
    elif map[check[0]][check[1]] == "#":
        # Turn right (clockwise)
        if dir == "U":
            dir = "R"
        elif dir == "R":
            dir = "D"
        elif dir == "D":
            dir = "L"
        elif dir == "L":
            dir = "U"
        continue  # Continue to the next iteration to check the new direction

print(len(unique))