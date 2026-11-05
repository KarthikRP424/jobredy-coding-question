def second_largest(nums):
    
    largest = float('-inf')
    sec_largest = float('-inf')
    
    n = len(nums)
    
    for i in range(0,n):
        
        if nums[i] > largest:
            
            sec_largest = largest
            
            largest = nums[i]
            
        elif nums[i] > sec_largest and nums[i] < largest:
            
            sec_largest = nums[i]
            
    return sec_largest


print(second_largest([10,20,30,40,50,60,70]))  # Output: 60