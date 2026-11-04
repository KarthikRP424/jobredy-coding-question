nums = [55, 23, 78, 12, 34, 90, -11]

largest = nums[0]

n = len(nums)

for i in range(0,n):
    
    largest = max(largest, nums[i])
    
print("The largest number in the list is:", largest)  # Output: The largest number in the list is: 90



def find_largest(num):
    largest = num[0]
    n = len(num)

    for i in range(0, n):
        largest = max(largest, num[i])

    return largest

print(find_largest([55, 23, 789, 121, 34, 99, -111]))  # Output: 90
