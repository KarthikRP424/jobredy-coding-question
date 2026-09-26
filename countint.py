# count the integer
import math as main

num = int(input("enter the number:"))


count = int(main.log10(num)+1)
    
print("the number of digits in the number is:", int(count)) 




# another way to count the integer

num = int(input("enter the number:"))

count = 0

while num > 0:
    num = num//10
    
    count+=1
    
print("the number of digits in the number is:", count)