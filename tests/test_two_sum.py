from leetcode_py.two_sum import Solution


def test_two_sum_1():
    # Arrange
    nums = [2, 7, 11, 15]
    target = 9
    output = [0, 1]

    # Act
    result = Solution().twoSum(nums, target)

    # Assert
    assert result == output


def test_two_sum_2():
    # Arrange
    nums = [3, 2, 4]
    target = 6
    output = [1, 2]

    # Act
    result = Solution().twoSum(nums, target)

    # Assert
    assert result == output


def test_two_sum_3():
    # Arrange
    nums = [3, 3]
    target = 6
    output = [0, 1]

    # Act
    result = Solution().twoSum(nums, target)

    # Assert
    assert result == output


def test_two_sum_4():
    # Arrange
    nums = [-10, -1, -18, -19]
    target = -19
    output = [1, 2]

    # Act
    result = Solution().twoSum(nums, target)

    # Assert
    assert result == output
