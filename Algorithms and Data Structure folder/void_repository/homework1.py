def avg(list):
    temp = 0
    count = 0
    avg = 0
    
    for i in range(len(list)):
        temp = temp + list[i]
        count = count + 1

        if count >= 3:
            avg = temp / 3
            print(avg)
            count = 0
        

array = [1,2,7,6,5,7]

print(avg(array))