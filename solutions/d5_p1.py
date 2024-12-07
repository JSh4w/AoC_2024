f = open("day_5.txt")
text = f.readlines()

rule = False
rules = {}
orders=[]
for line in text:
    if line in ['\n', '\r\n']:
        rule = True
        pass
    if rule:
        x=line.strip()
        x= x.split(",")
        order = [] 
        for i in x:
            order.append(i)
        orders.append(order)
    else:
        x = line.strip()
        ke, val = x.split("|")
        if ke not in rules.keys():
            rules[ke]=[val]
        else:
            rules[ke].append(val)
orders=orders[1:]
sum = 0 

for order in orders:
    good = True 
    for ix, val in enumerate(order):
        rule = rules[val]
        rule = tuple(rule)
        if ix == 0:
            rg  = [-1]
        else:
            rg = order[:ix]
            
        for i in rg:
            if i in rule:
                good = False
                
    if good:
        x = len(order)//2
        sum += int(order[x])
print(sum)