from leetcode_py.valid_anagram import Solution


def test_isAnagram_1():
    # Arrange
    solution = Solution()
    s, t = "anagram", "nagaram"
    output = True

    # Act
    result = solution.isAnagram(s, t)

    # Assert
    assert result == output


def test_isAnagram_2():
    # Arrange
    solution = Solution()
    s, t = "rat", "car"
    output = False

    # Act
    result = solution.isAnagram(s, t)

    # Assert
    assert result == output
