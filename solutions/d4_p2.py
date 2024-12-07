f = open("day_4.txt")
text = f.readlines()
m =[]
for i in text:
    m.append(i.strip())
ROWS = len(m)
COLS = len(m[0])
tot = 0
for i in range(ROWS-2):
    for j in range(COLS-2):
        if m[i][j] + m[i+1][j+1] + m[i+2][j+2] in ("MAS","SAM"):
            if m[i][j+2] + m[i+1][j+1] + m[i+2][j] in ("MAS", "SAM"):
                tot+=1
                
print(tot)