def singleDigit(N):
    sum = 0
    while (N != 0):
        sum = sum + (N % 10)
        N = N//10
    if sum>9:
        return singleDigit(sum)
    else:
        return sum