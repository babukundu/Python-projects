def nextRound(k,scores):
    count = 0
    for i in scores:
        if i >= scores[k-1] and scores[k-1]>0:
            count = count + 1
    if count<=20:
        return count
    else:
        return 20