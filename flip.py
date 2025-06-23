def flipnumbers(num1, num2):
    flips = 0
    
    while (num1 > 0 or num2 > 0):
        t1 = num1 & 1
        t2 = num2 & 1
        
        if (t1 != t2):
            flips += 1
            
        num1 >>= 1
        num2 >>= 1
        
    return flips

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"The number of flips reuired to make {num1} and {num2} equal is : {flipnumbers(num1, num2)}")