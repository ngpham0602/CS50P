from bank import greeting

def test1():
    assert greeting("Hello") == "$0"

def test2():
    assert greeting("H") == "$20"

def test3():
    assert greeting("What's up") == "$100"