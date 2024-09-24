input_dict = {
   1: ['hi', 'there', 'fred'], 
   2: ['there', 'we', 'go'],
   3: ['fred', 'was', 'there']}
tup = ()
for i in input_dict.keys():
    words = input_dict[i]
    for m in range(len(words)):
        tup = tup + (words[m],i)
# print(tup)
lst = list(tup)
# print(lst)
# print(type(lst))

counts = dict()
for m in range(0,len(lst)-1,2):
    w=lst[m]
    w_lst= list()
    for n in range(m+2,len(lst)-1,2):  
        if w in counts:
            w_lst.append(lst[m+1])
            counts[w] += w_lst
        else:
            w_lst=lst[m+1]
            counts[w] = w_lst

    res_dict = dict((k, v) for k, v in counts.items())
    print(lst[m])
print(res_dict)

