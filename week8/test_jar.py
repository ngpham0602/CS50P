from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    custom_jar = Jar(5)
    assert custom_jar.capacity == 5
    assert custom_jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError) as error:
        jar.deposit(13)
    assert str(error.value) == "There's more cookies than the jar needed!"
    print(f"{error.value}")

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    with pytest.raises(ValueError) as error:
        jar.withdraw(13)
    assert str(error.value) == "You take way too many cookies that the jar have!"
    print(f"{error.value}")