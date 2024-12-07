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
            val+=1
        else:
            for i in range(len(nums)):
                test = list(nums)
                test.pop(i)
                diffs = zip(test,test[1:])
                diffs = [(j-i) for i,j in diffs]
                incr = all( i in (1,2,3) for i in diffs)
                decr = all( i in (-1,-2,-3) for i in diffs)
                if incr or decr:
                    val+=1 
                    break  
            
    print(val)
        