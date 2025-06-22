import pytest
from datetime import date

def is_even(num):
    return num % 2 == 0

def test_is_even():
    assert is_even(6) == True
    assert is_even(11) == False
#============================================================================

class Person():
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def calc_age(self):
        return date.today().year - self.birthdate.year

@pytest.fixture(scope="session")
def person():
    dummy_person = Person("john", date(1997, 8, 11))
    return dummy_person

def test_person_class(person):
    assert person.calc_age() == 28

def test_person_name(person):
    assert person.name == "john"
    person.name = "George"
    assert person.name == "George"

def test_person_rename(person):
    assert person.name == "George"
#============================================================================

def multiply_numbers(num1, num2):
    return num1*num2

@pytest.mark.parametrize("num1, num2, result",
                         [[5, 10, 50],
                         [2, 4, 8],
                         [10, 2, 20]])
def test_sum_numbers(num1, num2, result):
    assert multiply_numbers(num1, num2) == result
#============================================================================

def divide_numbers(num1, num2):
    return num1 / num2

def test_divide_numbers():
    with pytest.raises(ZeroDivisionError):
        assert divide_numbers(1, 0)
#============================================================================

@pytest.mark.arithmetic1
def test_multiplication():
    assert 5 * 2 == 10

@pytest.mark.arithmetic1
def test_division():
    assert 10 / 2 == 5

@pytest.mark.arithmetic2
def test_addition():
    assert 2 + 2 == 4

@pytest.mark.arithmetic2
def test_substraction():
    assert  10 - 2 == 8
#============================================================================

@pytest.mark.xfail(reason="error on Linux, it's case-sensitive")
def test_something_else():
    name = "Temo"
    assert name == "temo"
#============================================================================

@pytest.mark.skip
def test_ignore():
    assert 5 + 5 == 10