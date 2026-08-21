from order_backward_a_string import word_backwards
import pytest


def test_word_backwards_work_with_long_string_and_special_character():
    #arrange
    my_input_string = "mnbvcxzlkjhgfdsapoiuytrewq1234567890!@#$%^&*()_+=-[]|{;',.<>}"

    #act
    inverted_string = word_backwards(my_input_string)
    compare_string = "}><.,';{|][-=+_)(*&^%$#@!0987654321qwertyuiopasdfghjklzxcvbnm"

    #assert
    assert inverted_string == compare_string


def test_word_backwards_work_with_long_string_numbers_and_empty_space():
    #arrange
    my_input_string = "God Of War is the #151654613 in the entire world."

    #act
    inverted_string = word_backwards(my_input_string)
    compare_string = ".dlrow eritne eht ni 316456151# eht si raW fO doG"

    #assert
    assert inverted_string == compare_string


def test_word_backwards_work_with_a_empty_string():
    #arrange
    my_input_string = ""

    #act & assert
    with pytest.raises(ValueError, match="Error: your variable is empty"):
        word_backwards(my_input_string)