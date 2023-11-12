from collections import defaultdict

# from typing import Counter


class Solutions:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Solution 1 : sorted string as key.
        map = defaultdict(list)
        for str in strs:
            sorted_str = "".join(sorted(str))
            map[sorted_str].append(str)
        return list(map.values())

        # Solution 2 : tuple containing the count of all characters as key
        # map = defaultdict(list)
        # for str in strs:
        #     character_count = Counter({key: 0 for key in range(26)})
        #     for character in str:
        #         character_count[ord(character) - ord("a")] += 1
        #     map[tuple(character_count.values())].append(str)
        # return list(map.values())
