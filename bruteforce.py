def bruteforce(num):
    
    result = []
    
    for i in range(1,num+1):
        
        if num % i == 0:
            
            result.append(i)
            
            
    return result

print(bruteforce(12))  # [1, 2, 3, 4, 6, 12]