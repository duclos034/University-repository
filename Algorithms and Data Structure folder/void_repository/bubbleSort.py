def bubbleSort(unsorted):
    
    n = len(unsorted)
    for i in range(len(unsorted) - 1):
        for j in range(n - 1 - i):
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]

    return unsorted

print(bubbleSort([5,4,3,1,10,7,6]))

