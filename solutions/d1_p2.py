with open("day_1.txt") as f:
    text = f.readlines()
    list_1 = []
    list_2 = []
    for i in text:
        numbers = i.split()
        list_1.append(int(numbers[0]))
        list_2.append(int(numbers[1]))
    num_dict= {}
    for num in list_2:
        try:
            num_dict[num] +=1
        except:
            num_dict[num] = 1 
    total = 0 
    for val in list_1:
        try:
            total += num_dict[val] * val
        except:
            continue
    print(total)