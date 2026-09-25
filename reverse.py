num = 12345

reverse = 0

while num > 0:
    
    lastdigit = num % 10
    num = num // 10
    reverse = reverse * 10 + lastdigit
    
    
print(reverse)
    
    
    
    