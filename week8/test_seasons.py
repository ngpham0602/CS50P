from seasons import convert

def test1():
    assert convert("1999-12-01") == "thirteen million four hundred eighty-seven thousand forty minutes"

def test2():
    assert convert("Jan 1 1999") == "Invalid date"

def test3():
    assert convert("1999-13-01") == "The year/month/day is out of range"

