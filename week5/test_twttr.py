from twttr import convert

def test1():
    assert convert("twitter") == "twttr"

def test2():
    assert convert("just setting up my twitter") == "jst sttng p my twttr"

def test3():
    assert convert("apple") == "ppl"

def test4():
    assert convert("aieou") == ""