from collections import defaultdict
f = open("inputs\day_7.txt")
input = f.readlines()


## must be a list in the case there are targets with the same value!!
equations = []
for line in input:
    goal, vals = line.split(":")
    vals = (vals.strip()).split(" ")
    equations.append([goal, [int(i) for i in vals]])


## -----
# We're trying to see if goal = y , can be made of some combinations vals(a,b,c,d) using + or * 
# Brute force try all combinations. Also check if product < goal then can never reach 
#
#
#
#
## -----
def combine(vals, symbols):
    tot = vals[0]
    for x, i in enumerate(symbols):
        if i == "*":
            tot = tot * vals[x+1]
        elif i == "+":
            tot = tot + vals[x+1]
        else:
            tot = int(str(tot) + str(vals[x+1]))
    return tot

        


tot = 0
idx =0 
for equation in equations:
    vals =  equation[1]
    k = int(equation[0])
    combinations  = len(vals) - 1
    symbols=["*","+","C"]
    def gen_combos(symbols,length):
        def generate_recursive(current, remaining_length):
            if remaining_length == 0:
                return [current]
            results = []
            for symbol in symbols:
                results.extend(generate_recursive(current + symbol, remaining_length - 1))
            return results
        return generate_recursive("", length)
    all_combos = gen_combos(symbols, combinations)
    for combo in all_combos:
        check = combine(vals, combo)
        if check == k:
            tot+= k
            break
    idx +=1
    if idx%50 == 0:
        print(f"{idx} done out of {len(equations)}")
print(tot)

        



