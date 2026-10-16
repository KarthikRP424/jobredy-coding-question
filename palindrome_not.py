def palindrome(s):
    
    n = len(s)
    
    left = 0
    
    right = n-1
    
    while left < right:
        
        
        if s[left] != s[right]:
            
            return False
        
        left += 1
        
        right -= 1
        
    return True

print(palindrome("malayalam"))  # True



#using palindrome 

def func(s,left,right):
    
    if left >= right:
        
        return True
    
    if s[left] != s[right]:
        
        return False
    
    return func(s,left+1,right-1)

print(func("malayalam",0,len("malayalam")-1))  # True