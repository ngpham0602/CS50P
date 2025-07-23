from numb3rs import validate

def test1():
    assert validate("1.1.1.1") == True

def test2():
    assert validate("512.512.512.512") == False

def test3():
    assert validate("1.2.3.1000") == False

def test4():
    assert validate("192.168.004.1") == False

def test5():
    assert validate("cat") == False