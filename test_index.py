from app import add

def test_add():
    assert add(9,5) == 14
    assert add(5, "sad") == "Invalid Input"