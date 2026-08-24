from search_prime_numbers import define_prime_number, prime_numbers, enter_numbers
import pytest


def test_define_prime_number_is_true_or_false():
    #arrange
    cases = [
        (-5, False),
        (0, False),
        (1, False),
        (2, True),     
        (3, True),
        (4, False),
        (9, False),
        (13, True),
        (25, False),   
        (29, True)
    ]

    #act
    for number, expected in cases:

        #assert
        assert define_prime_number(number) == expected


def test_prime_numbers_not_prime_numbers_and_negative_numbers():
    #arrange
    input_list = [1, 0, 4, 6, 8, 9, -1, -19, -8]

    #act
    result = prime_numbers(input_list)

    #assert
    assert result == "No prime number was found"


def test_prime_numbers_repeat_prime_numbers_and_repeat_non_prime_numbers():
    #arrange
    input_list = [1, 1, 2, 2, 53, 53, 8, 8, 97, 97, 10, 10, 11, 11, 11]

    #act
    result = prime_numbers(input_list)
    expected = [2, 2, 53, 53, 97, 97, 11, 11, 11]

    #assert
    assert result == expected


def test_enter_number_empty_value(monkeypatch):
    #arrange
    monkeypatch.setattr('builtins.input', lambda _: "")       

    #act & assert
    with pytest.raises(ValueError, match="Error you dont enter a value to check"):
        enter_numbers()

# I had to do some research to figure out how to simulate an input located 
# inside a `while` loop within the `enter_number` function 
# in order to check for a null value error, That’s how I found the monkeypatch