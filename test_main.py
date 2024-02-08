import main

def test_add():
    assert main.add(3, 4) == 7
    assert main.add(0, 0) == 0

def test_div():
    assert main.div(3, 0) == float("inf")