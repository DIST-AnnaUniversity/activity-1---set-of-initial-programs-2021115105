#to add the sum of digits in a number 
n=int(input("enter a number"))
tot=0
while(n>0):
    dg=n%10
    tot=tot+dg
    n=n//10
print("The total sum of digits is:",tot)
