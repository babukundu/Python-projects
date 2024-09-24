def series(x):
    sum1=0
    n=100
    for i in range(0,n+1):
        m=1/2**i
        if m>=x:
            sum1=sum1+(1/(2**i))
    
    return (round(sum1,4))
