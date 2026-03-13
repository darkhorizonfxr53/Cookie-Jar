import pytest
from jar import Jar

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    jar2 = Jar() # Default should be 12
    assert jar2.capacity == 12
    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.deposit(10)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(10)
