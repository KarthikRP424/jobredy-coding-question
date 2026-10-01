class Solution(object):
    def findMaxAverage(self, nums, k):

        # Sum of the first window
        window_sum = sum(nums[:k])

        # Maximum sum found so far
        max_sum = window_sum

        # Slide the window
        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        # Maximum average
        return float(max_sum) / k
    
    
print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))