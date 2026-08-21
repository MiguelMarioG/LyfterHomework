from class_math_operation import MathOperation
import pytest
import unittest


def test_math_operation_with_positive_numbers():
    #arrange
    first_value = 8
    second_value = 5

    #act
    operation = MathOperation(first_value, second_value)
    result = operation.multiplication()

    #assert
    assert result == 40


def test_math_operation_with_negative_numbers():
    #arrange
    first_value = -30
    second_value = -20

    #act
    operation = MathOperation(first_value, second_value)
    result = operation.addition()

    #assert
    assert result == -50


def test_math_operation_with_a_cero_value():
    #arrange
    first_value = 0
    second_value = 0

    #act
    operation = MathOperation(first_value, second_value)
    result = operation.subtraction()

    #assert
    assert result == 0


def test_math_operation_divide_two_positive_numbers():
    #arrange
    first_value = 10
    second_value = 2

    #act
    operation = MathOperation(first_value, second_value)
    solution = operation.divide()

    #assert
    assert solution == 5.0


def test_math_operation_in_case_of_divide_with_cero():
    #arrange
    first_value = 8
    second_value = 0

    #act & assert
    operation = MathOperation(first_value, second_value)
    with pytest.raises (ValueError, match="You cannot divide by zero"):
        operation.divide()


def test_math_operation_in_case_of_a_string_value_raise_a_type_error():
    #arrange
    first_value = 18
    second_value = "python"

    #act & assert
    with pytest.raises(TypeError, match="String variables cannot be divided"):
        operation = MathOperation(first_value, second_value)