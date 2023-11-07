from typing import Counter


class Solution:
    # Solution 1
    # def isAnagram(self, s: str, t: str) -> bool:
    #     map = [0] * 26

    #     for x in s:
    #         map[ord(x) - ord("a")] += 1
    #     for x in t:
    #         map[ord(x) - ord("a")] -= 1
    #     for x in map:
    #         if x != 0:
    #             return False

    #     return True

    # Solution 2
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        return s_counter == t_counter
