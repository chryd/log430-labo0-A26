"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

def test_add_success():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 5

# def test_add_failure():
#     my_calculator = Calculator()
#     assert my_calculator.addition(2, 3) == 6

def test_sub_success():
    my_calculator = Calculator()
    assert my_calculator.subtraction(5, 3) == 2

# def test_sub_failure():
#     my_calculator = Calculator()
#     assert my_calculator.subtraction(5, 3) == 3

def test_mult_success():
    my_calculator = Calculator()
    assert my_calculator.multiplication(2, 3) == 6

# def test_mult_failure():
#     my_calculator = Calculator()
#     assert my_calculator.multiplication(2, 3) == 7

def test_div_success():
    my_calculator = Calculator()
    assert my_calculator.division(6, 3) == 2

# def test_div_failure():
#     my_calculator = Calculator()
#     assert my_calculator.division(6, 3) == 3