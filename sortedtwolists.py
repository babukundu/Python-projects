lst = [-5, -23, 5, 0, 23, -6, 23, 67]
lst1=['ai','yv','fe','uo','ep','on','pm','qs']
zipped_lists = zip(lst, lst1)
sorted_pairs = sorted(zipped_lists,reverse=True,key=lambda x:x[0])

tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]
print(list1)
print(list2)