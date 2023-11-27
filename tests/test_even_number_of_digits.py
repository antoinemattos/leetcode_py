from leetcode_py.even_number_of_digits import Solution


def test_find_even_number_of_digits_1() -> None:
    # Arrange
    input = [12, 345, 2, 6, 7896]
    output = 2

    # Act
    result = Solution().find_even_number_of_digits(input)

    # Assert
    assert result == output


def test_find_even_number_of_digits_2() -> None:
    # Arrange
    input = [555, 901, 482, 1771]
    output = 1

    # Act
    result = Solution().find_even_number_of_digits(input)

    # Assert
    assert result == output
