from um import count

def test1():
    assert count("um") == 1

def test2():
    assert count("um?") == 1

def test3():
    assert count("Um, thanks for the album.") == 1

def test4():
    assert count("Um, thanks um...") == 2