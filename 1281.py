# Subtract the Product and Sum of Digits of an Integer


def subtractProductAndSum(n):
    
    
    num = n
    
    product = 1
    
    total = 0
    
    
    while  num > 0:
        
        last_digit = num % 10
        
        product = product * last_digit
        
        total += last_digit
        
        num = num // 10
        
    return product - total


print(subtractProductAndSum(234))