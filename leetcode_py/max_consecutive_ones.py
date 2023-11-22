class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        # Solution 1 : O(n) time, O(1) space
        max_consecutive_ones, current_streak = 0, 0
        for n in nums:
            if n == 1:
                current_streak += 1
            else:
                max_consecutive_ones = max(max_consecutive_ones, current_streak)
                current_streak = 0
        return max(max_consecutive_ones, current_streak)
