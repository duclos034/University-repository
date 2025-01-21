def divideInput(a,low,high):
    pivot = a[high]
    i = low
    j = low
    while j < high:
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1
    
    a[i], a[j] = a[j], a[i]
    return i


def quickSort(a,low,high):
    if low < high:
        pivot = a[high]
        pivotIndex = divideInput(a, low, high)
        quickSort(a,low, pivotIndex - 1)
        quickSort(a, pivotIndex + 1, high)


myList = [5,4,3,1,2,7,6,8]
quickSort(myList,0,len(myList) - 1)
print(myList)