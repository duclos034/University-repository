def mergeSort(myList):
    if len(myList) > 1:

        left = myList[0:len(myList)//2]
        right = myList[len(myList)//2:]
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while(i < len(left) and j < len(right)):
            if left[i] < right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1 
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i+=1
            k+=1
        while(j < len(right)):
            myList[k] = right[j]
            j+=1
            k+=1       
    

inputList = [3,2,1,4,5,0,7,6]
mergeSort(inputList)
print(inputList)