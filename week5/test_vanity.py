from vanity import is_valid

def test1():
    assert is_valid("CS50") == "Valid"

def test2():
    assert is_valid("CS05") == "Invalid"

def test3():
    assert is_valid("CS50P") == "Invalid"

def test4():
    assert is_valid("PI3.14") == "Invalid"

def test5():
    assert is_valid("H") == "Invalid"

def test6():
    assert is_valid("OUTATIME") == "Invalid"

