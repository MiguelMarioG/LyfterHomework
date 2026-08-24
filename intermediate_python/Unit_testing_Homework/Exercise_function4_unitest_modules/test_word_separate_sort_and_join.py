from word_separate_sort_and_join import separate_word, sort_word
import pytest


def test_separate_word_including_integer_and_symbols():
    #arrange
    word_to_separate = "c0mput3r-a1rp1an3-funct10n-m0n1t0r-tra1n-pyth0n-var1abl3-z10n"

    #act
    result_word = separate_word(word_to_separate)
    compare_word = ['c0mput3r', 'a1rp1an3', 'funct10n', 'm0n1t0r', 'tra1n', 'pyth0n', 'var1abl3', 'z10n']

    #assert
    assert result_word == compare_word


def test_separate_word_with_a_empty_value():
    #arrange
    word_to_separate = "PYTHON-"

    #act & assert
    with pytest.raises (ValueError, match="Error: cannot split empty values"):
        separate_word(word_to_separate)


def test_sort_word_with_upper_and_duplicate_words():
    #arrange
    word_to_sort = ['ZebrA', 'ApplE', 'ZebrA', 'PYTHON', 'AirplanE', 'MonitoR']

    #act
    sorted_word = sort_word(word_to_sort)
    compare_word = 'AirplanE-ApplE-MonitoR-PYTHON-ZebrA-ZebrA'

    #assert
    assert sorted_word == compare_word


def test_separate_word_a_empty_word():
    #arrange
    word_to_separate = ""

    #act & assert
    with pytest.raises(ValueError, match="Error: It is an empty value"):
        separate_word(word_to_separate)