class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Solution 1
        # map = [(x, i) for i, x in enumerate(nums)]
        # map.sort()

        # start, end = 0, len(map) - 1
        # while start != end:
        #     if map[start][0] + map[end][0] == target:
        #         return sorted([map[start][1], map[end][1]])
        #     elif map[start][0] + map[end][0] > target:
        #         end -= 1
        #     elif map[start][0] + map[end][0] < target:
        #         start += 1

        # return []

        # Solution 2
        map = {x: i for i, x in enumerate(nums)}
        for i, x in enumerate(nums):
            value_to_search = target - x
            if value_to_search in map and i != map[value_to_search]:
                return [i, map[value_to_search]]

        return []
