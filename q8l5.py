def my_enumerate(items):
    lst=[]
    for n in range(0, len(items)):
        tupl=(n, items[n])
        lst.append(tupl)
    return lst
