from fuel import convert
import pytest

def test1():
    assert convert("3/4") == "75%"

def test2():
    assert convert("1/4") == "25%"

def test3():
    assert convert("4/4") == "F"

def test4():
    assert convert("0/4") == "E"

def test5():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test6():
    with pytest.raises(ValueError):
        convert("three/four")

def test7():
    with pytest.raises(ValueError):
        convert("1.5/3")

def test8():
    with pytest.raises(ZeroDivisionError):
        convert("-3/4")

def test9():
    with pytest.raises(ValueError):
        convert("5/4")