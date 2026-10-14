def num(n):
    
    total = 0
    
    for i in range(0,n+1):
        
        total += i
        
    return total

print(num(5))  # Output: 15


def func(sum,i,n):
    
    if i > n:
        return sum
    
    sum += i
    
    return func(sum,i+1,n)

print(func(0,1,5))  # Output: 15