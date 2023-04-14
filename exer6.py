 #count the number of digits for the given number 
 num = int(input("Enter a number: "))  

count = 0  

while num > 0:   
    count += 1   
    num //= 10  

print("Number of digits:", count)
