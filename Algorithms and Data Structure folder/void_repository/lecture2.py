def findMaxSumPath(a,b):
    i = 0
    j = 0
    sum1 = 0
    sum2 = 0
    result = 0
    while(i < len(a) and j < len(b)):
        if a[i] < b[j]:
            sum1 = sum1 + a[i]
            i = i + 1
        elif b[j] > a[i]:
            sum2 = sum2 + b[j]
            j = j + 1 
        else:
            result = result + max(sum1, sum2) + a[i]
            sum1 = 0
            sum2 = 0    
            i = i + 1
            j = j + 1 