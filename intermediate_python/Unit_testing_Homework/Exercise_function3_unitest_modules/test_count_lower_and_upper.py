from count_lower_and_upper import count_lower_and_upper
import pytest


def test_count_lower_and_upper_can_count_all_upper_and_symbols():
    #arrange
    input_wrod = "PYTHON_#1_CODING"

    #act
    total_upper = count_lower_and_upper(input_wrod)

    #assert
    assert total_upper == "There's 12 upper cases and 0 lower cases"


def test_count_lower_and_upper_can_count_all_lower_and_numbers_and_symbols():
    #arrange
    input_word = "python_928374928374?----hello world"

    #act
    total_lower = count_lower_and_upper(input_word)

    #assert
    assert total_lower == "There's 0 upper cases and 16 lower cases"


def test_count_lower_and_upper_dont_accept_empty_string_value():
    #arrange
    input_word = ""

    #act & assert
    with pytest.raises(ValueError, match="Error: cannot count a null value"):
        count_lower_and_upper(input_word)