m = [2,3,4,5,2,6,7,8,9,1,2,3,4,5,6,7,8,9]

n = [1,2,3,4,5,6,7,8,9]

frequency_map = {}

for num in m:
    
    if num in frequency_map:
        frequency_map[num] += 1
        
    else:
        frequency_map[num] = 1
        
for num in n:
    
    if num in frequency_map:
        print(frequency_map[num])
        
    else:
        print(0)
        
print(frequency_map)