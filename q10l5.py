def composite2(N):
    M = 1
    Max = 1000
    counter = 0
    for number in range(M,Max+1):
        count = 0
        for divider in range(2,number//2+1):
            if number%divider == 0:
                count+=1
        if count >= 1 and number%2!=0:
            counter+=1
            if counter == N:
                return number
    
