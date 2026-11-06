def sorteddor_not(nums):
    
    
    n = len(nums)
    
    for i in range(0,n-1):
        
        if nums[i] > nums[i+1]:
            
            
            return False
        
    return True

print(sorteddor_not([1,2,3,4,5,1]))  # Output: True