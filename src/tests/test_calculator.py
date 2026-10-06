"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Hugo Barou, Amélie Lemay, Martin Simon, Christine Yang-Dai, 2026
"""

from calculator import Calculator

my_calculator = Calculator()

def test_app():
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

def test_addition(): 
    assert my_calculator.addition(1,1) == 2

def test_subtraction():
    my_calculator = Calculator()
    assert my_calculator.subtraction(1,1) == 0

def test_multiplication():
    my_calculator = Calculator()
    assert my_calculator.multiplication(1,10) == 10

def test_division():
    my_calculator = Calculator()
    assert my_calculator.division(10,2) == 5