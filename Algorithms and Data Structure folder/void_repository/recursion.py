def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
        

def powerFinder(a, n):
    if n == 0:
        return 1
    else:
        return a * pow(a, n -1)
  

def fibbing(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:        
        return fibbing(n - 1) + fibbing(n - 2)
    

N = 20
result = [-1] * N 
def superFib(n):
    if result[n] != -1:
        return result[n]
    else:
        if n <= 1:
            return n
        else:
            if result[n - 1] == -1:
                result[n - 1 ] = superFib(n - 1)

            if result[n - 2] == -1:
                result[n - 2] = superFib(n - 2)

            return result[n - 1] + result[n - 2]
        
def ultraFib(n):
    if n <= 1:
        return(0, n)
    else:
        a, b = ultraFib(n -1)
        return(b, a + b)
        

# a * a^n - 1

def dukeSearch(a, low, high, y):
   
    if low > high:
        return False
    else:
        mid = (low + high) //2
        if a[mid] == y:
            return True
        elif a[mid] > y:
            return dukeSearch(a, low, mid - 1, y)
        else:
            return dukeSearch(a, mid + 1, high, y)

a = [5,8,10,11,31,60,62,70]

print(dukeSearch(a, 0, len(a) - 1, 5))



    
   






