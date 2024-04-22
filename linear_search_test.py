from linear_search import linear_search

def test_empty():
    assert linear_search([], 0) == -1

def test_1():
    a = [45, 67, -2, 33, -44, 134, -67]
    assert linear_search(a, 1) == -1

def test_0():
    a = [45, 67, -2, 33, -44, 134, -67]
    assert linear_search(a, 0) == -1

def test__1():
    a = [45, 67, -2, 33, -44, 134, -67]
    assert linear_search(a, -1) == -1

def test_2():
    a = [45, 67, -2, 33, -44, 134, -67]
    assert linear_search(a, 2) == -1

def test__2():
    a = [45, 67, -2, 33, -44, 134, -67]
    assert linear_search(a, -2) == 2

def test_134():
    a = [45, 67, -2, 33, -44, 134, -67]
    assert linear_search(a, 134) == 5

def test_67():
    a = [45, 67, -2, 33, -44, 134, -67]
    assert linear_search(a, 67) == 1

def test__67():
    a = [45, 67, -2, 33, -44, 134, -67]
    assert linear_search(a, -67) == 6

def test_first():
    a = [1, 1, 1, 2, 2, 2, 2, 2, 2]
    assert linear_search(a, 2) == 3

def test_first1():
    a = [1, 1, 1, 2, 2, 2, 2, 2, 2]
    assert linear_search(a, 1) == 0

def test_last():
    a = [1, 1, 1, 2, 2, 2, 2, 2, 2, 3]
    assert linear_search(a, 3) == 9

