# fibonacci  using recursion
def fibonacci(nums):
    
    if nums == 0 or nums ==1:
        
        return nums
    
    return fibonacci(nums-1) + fibonacci(nums-2)

print(fibonacci(9))  # 5