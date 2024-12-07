f = open("day_4.txt")
text = f.readlines()
m =[]
for i in text:
    m.append(i.strip())
ROWS = len(m)
COLS = len(m[0])
tot = 0
for i in range(ROWS):
    for j in range(COLS):
        #ROWS
        if i < ROWS -3:
            if m[i][j] + m[i+1][j] + m[i+2][j] + m[i+3][j] in ("XMAS","SAMX"):
                tot +=1 
        #COLS
        if j < COLS -3:
            if m[i][j:j+4] in ("XMAS","SAMX"):
                tot +=1
        
        #DIAGONAL RIGHT
        if j < COLS -3 and i < ROWS -3: 
            if m[i][j] + m[i+1][j+1] + m[i+2][j+2] + m[i+3][j+3] in ("XMAS","SAMX"):
                tot +=1
        #DIAGONAL LEFT
        if j > 2 and i < ROWS -3: 
            if m[i][j] + m[i+1][j-1] + m[i+2][j-2] + m[i+3][j-3] in ("XMAS","SAMX"):
                tot +=1
print(tot)