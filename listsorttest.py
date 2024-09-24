lst = [-5, -23, 5, 0, 23, -6, 23, 67]
lst1=['a','y','f','u','e','o','p','q']

lst, lst1 = zip(*sorted(zip(lst, lst1),reverse=True))

print(lst)
print(lst1)