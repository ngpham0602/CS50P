from working import convert

def test1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test3():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"

def test4():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test5():
    assert convert("9:60 AM to 5:60 PM") == "Invalid time format"

def test6():
    assert convert("9 AM - 5 PM") == "Invalid time format"

def test7():
    assert convert("09:00 AM - 17:00 PM") == "Invalid time format"