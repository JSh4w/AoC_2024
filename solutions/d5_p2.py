f = open("day_5.txt")
text = f.readlines()
from collections import defaultdict


def topo_sort(update, rus):
    this_rules =[] 
    for i in update:
        #for each value in wrong list
        for k in rus[i]:
            # for each order from value i 
            if k in set(update):
                # if order in update
                this_rules.append((i,k))
                #add to orders
    indegree = defaultdict(int)
    for x,y in this_rules:
        indegree[y] += 1 
    
    ans =[] 
    while len(ans) < len(update):
        # ans = len of update
        for a in update:
            if a in ans:
                continue
            if indegree[a] <= 0:
                ans.append(a)
                for x,y in this_rules:
                    if x == a:
                        indegree[y] -= 1
                        
    return ans

                 

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
p2 = 0 

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
    else:
        sorted = topo_sort(order, rules)
        p2 += int(sorted[len(sorted)//2])
    print("done")
    
print(p2)