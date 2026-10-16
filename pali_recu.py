

def func(s,left,right):
    
    if left >= right:
        
        return True
    
    if s[left] != s[right]:
        
        return False
    
    return func(s,left+1,right-1)

print(func("malayalam",0,len("malayalam")-1))  # True