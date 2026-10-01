n = 11

hash_list = [0]*n

m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 1, 4, 5, 6, 7, 8, 9]

k = [1, 2, 3, 4, 5, 6, 77, 7, 77, 89, 9]


for num in m:
    hash_list[num] += 1
    
for num in k:
    if num < 1 or num > 10:
        print(0)
            
    else:
        print(hash_list[num])
            
print(hash_list)