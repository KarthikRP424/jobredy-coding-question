def frequency_maping(nums):
    
    n = len(nums)
    
    
    hash_map = {}
    
    for i in range(0,n):
        hash_map[nums[i]] = hash_map.get(nums[i],0)+1
        
    return hash_map


print(frequency_maping([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]))  # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2}