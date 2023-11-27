from math import floor, log10


class Solution:
    def find_even_number_of_digits(self, nums: list[int]) -> int:
        # Solution 1, time:O(n), space:O(1)
        # result, number_of_digits = 0, 1
        # for n in nums:
        #     number_of_digits = 1
        #     while n // 10 != 0:
        #         number_of_digits += 1
        #         n = n // 10
        #     result += number_of_digits % 2 == 0
        # return result

        # Solution 2, time:O(n), space:O(1)
        # return sum(
        #     1
        #     for n in nums
        #     if (n > 9 and n < 100) or (n > 999 and n < 10000) or n == 100000
        # )

        # Solution 3, time:O(n), space:O(1)
        # result = 0
        # for n in nums:
        #     if (n > 9 and n < 100) or (n > 999 and n < 10000) or n == 100000:
        #         result += 1
        # return result

        # Solution 4, time:O(n), space:O(1)
        result = 0
        for n in nums:
            number_of_digits = floor(log10(n)) + 1
            if number_of_digits % 2 == 0:
                result += 1
        return result
