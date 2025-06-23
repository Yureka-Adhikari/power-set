import math
def printpowerset(set, setsize):
    
    powerset_size = int(math.pow(2, setsize))
    outer = 0
    inner = 0
    
    for outer in range(powerset_size):
        for inner in range(setsize):
            if (outer & (1 << inner) >0):
                print(set[inner], end = "")
                
        print()
        
size = int(input("Enter the size of the set : "))
set = []

for i in range(size):
    n = int(input("Enter the element : "))
    set.append(n)
    
printpowerset(set, size)
        
        
        