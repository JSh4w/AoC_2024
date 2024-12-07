with open("day_2.txt") as f:
    text = f.readlines()
    val = 0 
    for i in text:
        nums = i.split()
        nums = [int(num) for num in nums]
        diffs = zip(nums,nums[1:])
        diffs = [(j-i) for i,j in diffs]
        incr = all( i in (1,2,3) for i in diffs)
        decr = all( i in (-1,-2,-3) for i in diffs)
        if incr or decr:
            print(nums,diffs)
            val+=1
            
    print(val)
        