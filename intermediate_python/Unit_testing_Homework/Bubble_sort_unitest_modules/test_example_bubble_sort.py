from example_bubble_sort import bubble_sort
import pytest


def test_bubble_sort_work_with_a_small_list():
    #arrange
    input_list = [
        42, 15, 88, 7, 23, 91, 54, 12,
        99, 5, 18, 76, 31, 84, 10
    ]
    expected_list = sorted(input_list)

    #act
    bubble_sort(input_list)

    #assert
    assert input_list == expected_list


def test_bubble_sort_work_with_a_list_bigger_the_100_values():
    #arrange
    input_list = [
    84, 12, 95, 33, 47, 61, 2, 78, 19, 50, 91, 28, 64, 5, 39,
    73, 16, 88, 42, 99, 23, 56, 10, 81, 35, 67, 4, 92, 18, 53,
    76, 29, 62, 8, 44, 87, 21, 58, 96, 31, 70, 14, 83, 37, 65,
    1, 94, 25, 52, 79, 11, 46, 89, 34, 68, 6, 90, 24, 59, 97,
    15, 82, 38, 71, 3, 93, 27, 55, 80, 13, 48, 86, 32, 66, 9,
    74, 17, 60, 98, 22, 57, 41, 77, 30, 63, 7, 85, 20, 51, 100,
    45, 72, 26, 54, 88, 14, 69, 36, 91, 3, 49, 82, 28, 61, 95,
    19, 53, 78, 10, 43, 87, 24, 67, 2, 99, 35, 70, 16, 58, 92,
    31, 64, 8, 46, 83, 27, 60, 94, 18, 52, 75, 12, 40, 89, 23,
    56, 97, 34, 68, 5, 81, 15, 48, 90, 21, 63, 96, 29, 73, 11
]
    expected_list = sorted(input_list)

    #act
    bubble_sort(input_list)

    #assert
    assert input_list == expected_list


def test_bubble_sort_work_with_a_empty_list():
    #arrange
    input_list = []

    #act & assert
    with pytest.raises(ValueError, match="The list is empty"):
        bubble_sort(input_list)


def test_bubble_sort_work_with_a_invalid_value():
    #arrange
    input_list = [4, "hello", 10]

    #act & assert
    with pytest.raises(ValueError, match="The list contain invalid values"):
        bubble_sort(input_list)


def test_bubble_sort_dont_work_with_values_different_then_a_list():
    #arrange
    value = 9201986

    #act & assert
    with pytest.raises(TypeError, match="Values ​​that are not a list cannot be used"):
        bubble_sort(value)