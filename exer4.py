#to count the number of vowels 
str=input("enter string:")
count=0
for i in str:
    if i in "AEIOUaeiou":
        count+=1
print(count)
