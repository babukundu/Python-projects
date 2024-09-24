def run_length_encode(nums):
    lst=[]
    countnum=0
    set_nums = [] 
    for i in nums: 
        if i not in set_nums: 
            set_nums.append(i)
    for num in set_nums:
            countnum=nums.count(num)
            tupl=(num,countnum)
            lst.append(tupl)
    return lst

