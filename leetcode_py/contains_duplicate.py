class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # solution 1, time O(n), space O(n)
        # num_set = set()
        # for num in nums:
        #     if num in num_set:
        #         return True
        #     else:
        #         num_set.add(num)
        # return False

        # solution 2, time O(n), space O(n)
        return len(set(nums)) != len(nums)
