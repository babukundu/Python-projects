def lstround(lst):
    tup=()
    tuplst=[]
    for x in lst:
        a=round(x[1],4)
        tup=(x[0],a)
        tuplst.append(tup)
    print(tuplst)