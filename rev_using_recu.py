def func(nums, left, right):
    if left >= right:
        return

    nums[left], nums[right] = nums[right], nums[left]
    func(nums, left + 1, right - 1)

nums = [1, 2, 3, 4, 5]
func(nums, 0, len(nums) - 1)
print(nums)