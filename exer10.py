#to print the series of numbers
x = int(input("Enter the value of x: "))  
n = int(input("Enter the value of n: "))

res = 0  

 
for i in range(n+1):
    res+= x**i   

print("The value of 1+x+x**2+x**3+...+x^n is:", res)  
