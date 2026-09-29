


def frequency_maping(nums):
    
    freq_map = {}
    
    
    for i in range(0,len(nums)):
        
        if nums[i] in freq_map:
            
            freq_map[nums[i]] +=1
            
        else:
            
            freq_map[nums[i]] = 1
            
    return freq_map


print(frequency_maping([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]))  # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2}