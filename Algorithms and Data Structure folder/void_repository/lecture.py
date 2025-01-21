#write this at home


myList = [1,3,5,10,20,15,10,1]

#indec 4 is the peak element

def peak(list):
    isPeak = True
    peak = list[0]
    for i in range(1, len(list) - 1):
        if list[i - 1] < list[i] and list[i] > list[i + 1]:
            peak = i
        elif list[i - 1] < list[i] < list[i + 1] or list[i - 1] > list[i] > list[i + 1]:
            continue
        else:
            isPeak = False 
            peak = -1
            break
    return peak
         
    
mylist = [1,2,3,4,5,10,5,4,3,2,1]
print( peak(myList))
   

