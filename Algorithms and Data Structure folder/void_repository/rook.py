# add an element to the end of a list
#for each run of the code, you would need to have an empty part of the list and continute to add more to the 
#end 
def append(array, input):
    temp = [input]
    array = array + temp
    return array 

array = [1,5,6,7,8,9,10]
input = "Input"

def remove(array, index):
    length = len(array)
    if index >= length:
        return False
    for i in range(index + 1, length):
        array[i] = array[i + 1]
    array[length - 1] = None
    length = length - 1
    return True
print(append(array, input))
print(remove(array, 2))