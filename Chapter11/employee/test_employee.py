from employee import Employee
import pytest


@pytest.fixture
def employee():
    return Employee("John", "Doe", 5000)


def test_give_default_raise():
    employee = Employee("John", "Doe", 5000)
    employee.give_raise()
    assert employee.annual_salary == 10_000


def test_give_custom_raise():
    employee = Employee("John", "Doe", 5000)
    employee.give_raise(10_000)
    assert employee.annual_salary == 15_000


def test_give_default_raise_with_fixture(employee):
    employee.give_raise()
    assert employee.annual_salary == 10_000


def test_give_custom_raise_with_fixture(employee):
    employee.give_raise(10_000)
    assert employee.annual_salary == 15_000
