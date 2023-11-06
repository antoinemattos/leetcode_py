from leetcode_py.contains_duplicate import Solution


def test_example_1():
    # Arrange
    solution = Solution()
    input = [1, 2, 3, 1]
    output = True

    # Act
    result = solution.containsDuplicate(input)

    # Assert
    assert result == output


def test_example_2():
    # Arrange
    solution = Solution()
    input = [1, 2, 3, 4]
    output = False

    # Act
    result = solution.containsDuplicate(input)

    # Assert
    assert result == output


def test_example_3():
    # Arrange
    solution = Solution()
    input = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    output = True

    # Act
    result = solution.containsDuplicate(input)

    # Assert
    assert result == output
