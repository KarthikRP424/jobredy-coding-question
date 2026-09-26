n = 153

num = n

total = 0

node = len(str(num))


while num > 0:
    
    lastdigit = num % 10
    
    total += lastdigit ** node
    
    num = num // 10
    
    
print(total == n)  # True for 153, False for 123