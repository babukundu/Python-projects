def sequence(n):
    lst = []
    lst.append(n)
    while n>1:
        if n%2 == 0:
            m=n//2
            n=n//2
        else:
            m=n*3+1
            n=n*3+1
        lst.append(m)

    return lst