# nums[4,1,2,3,7,6,8]

def partition(nums,low,high):
    
    pivot = nums[low]
    
    i = low + 1
    j = high
    
    while i < j:
        
        while nums[i] <= pivot and i < high:
            
            i += 1
            
        while nums[j] > pivot and j > low:
            
            j -= 1
            
            
        if i < j:
            
            nums[i],nums[j] = nums[j],nums[i]
            
    nums[low],nums[j] = nums[j],nums[low]
    
    return j
    
    
def quick_sort(nums,low,high):
    
    if low < high:
        
        pivot_index = partition(nums,low,high)
        
        quick_sort(nums,low,pivot_index-1)
        
        quick_sort(nums,pivot_index+1,high)
        
    return nums

print(quick_sort([5,4,3,2,1],0,4))  # [1, 2, 3, 4, 5]
    