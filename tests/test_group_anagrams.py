from leetcode_py.group_anagrams import Solutions


def test_group_anagrams_1() -> None:
    # Arrange
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    # Act
    result = Solutions().groupAnagrams(input)

    # Assert
    for output_item in output:
        output_item.sort()
    output.sort()

    for result_item in result:
        result_item.sort()
    result.sort()

    assert output == result


def test_group_anagrams_2() -> None:
    # Arrange
    input = [""]
    output = [[""]]

    # Act
    result = Solutions().groupAnagrams(input)

    # Assert
    assert result == output


def test_group_anagrams_3() -> None:
    # Arrange
    input = ["a"]
    output = [["a"]]

    # Act
    result = Solutions().groupAnagrams(input)

    # Assert
    assert result == output
