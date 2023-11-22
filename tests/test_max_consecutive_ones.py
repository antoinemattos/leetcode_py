from leetcode_py.max_consecutive_ones import Solution


def test_max_consecutive_ones_1() -> None:
    # Arrange
    input = [1, 1, 0, 1, 1, 1]

    # Act
    result = Solution().findMaxConsecutiveOnes(input)

    # Assert
    assert result == 3


def test_max_consecutive_ones_2() -> None:
    # Arrange
    input = [1, 0, 1, 1, 0, 1]

    # Act
    result = Solution().findMaxConsecutiveOnes(input)

    # Assert
    assert result == 2
