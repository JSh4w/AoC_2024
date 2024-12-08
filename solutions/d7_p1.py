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

tot = 0
for equation in equations:
    vals =  equation[1]
    k = int(equation[0])
    combinations  = len(vals) - 1
    symbols=["*","+"]
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
        check = vals[0] 
        attempt = str(check)
        for num,i in enumerate(combo):
            if i == "*":
                check = check * vals[num+1]
            else:
                check = check + vals[num+1]
            attempt = attempt + i + str(vals[num+1])
        if check == k:
            tot+= k
            break
print(tot)

        



