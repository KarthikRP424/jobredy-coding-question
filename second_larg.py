nums = [10,20,30,40,50,60,70]

nums.sort()

print("The second largest number in the list is:", nums[-2])  # Output: The second largest number in the list is: 50


#method 2


num = [10,20,30,40,50,60,70]

largest = float('-inf')
second_largest = float('-inf')

n = len(nums)

for i in range(0,n):
    
    largest = max(largest, num[i])
    
for i in range(0,n):
    
    if num[i] > second_largest and num[i] < largest:
        
        second_largest = num[i]
        
print("The second largest number in the list is:", second_largest)  # Output: The second largest number in the list is: 60