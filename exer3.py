#to print the sum of n numbers 
n = int(input("Enter the value of n: "))  

sum = 0  # initialize sum to 0

 
for i in range(1, n+1):
    sum += i

print("The sum of first", n, "numbers is", sum)   
 
