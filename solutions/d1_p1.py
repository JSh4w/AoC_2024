with open("day_1.txt") as f:
    text = f.readlines()
    list_1 = []
    list_2 = []
    for i in text:
        numbers = i.split()
        list_1.append(numbers[0])
        list_2.append(numbers[1])
    list_1.sort()
    list_2.sort()
    distance = 0 
    for ix, val in enumerate(list_1):
       distance += abs(int(val) - int(list_2[ix]))
       
    print(distance)
