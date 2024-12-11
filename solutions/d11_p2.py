from functools import cache

with open("inputs/d11.txt", "r") as f:
    text = f.readline()
    text = text.split()
# need to make it a list of values
from functools import cache

@cache
def stone_c(num, iters) -> int:
    if iters == 0 :
        return 1
    ##zeroes can get left stripped to nothing so need to take into account
    if num == "0" or num == "":
        return stone_c("1", iters -1 )

    if len(num)%2 != 0:
        new_val = str(int(num)*2024)
        return stone_c(new_val, iters -1)
    
    return stone_c(num[:len(num)//2],iters -1) + stone_c(num[len(num)//2:].lstrip("0"), iters-1) 

print(sum(stone_c(val, 75) for val in text))