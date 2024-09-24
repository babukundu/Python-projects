def run_length_encode(nums):
    lst=[]
    countnum=0
    counts = dict()
    for num in nums:
        if num in counts:
        
        else:
            countnum=nums.count(num)
            tupl=(num,countnum)
            lst.append(tupl)            
    print(lst)
