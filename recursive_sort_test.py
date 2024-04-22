from recursive_sort import recursive_sort

def test_empty():
    a = []
    e = sorted(a)
    assert recursive_sort(a) == e

def test_1():
    a = [45, 67, -2, 33, 0, -44, 134, -67]
    e = sorted(a)
    assert recursive_sort(a) == e

def test_in_order():
    a = [i for i in range(10)]
    e = sorted(a)
    assert recursive_sort(a) == e

def test_reverse_order():
    a = [i for i in range(10,-1, -1)]
    e = sorted(a)
    assert recursive_sort(a) == e

def test_2():
    a = [i for i in range(-10,-1, 1)] + [i for i in range(10,-1, -1)]
    e = sorted(a)
    assert recursive_sort(a) == e

def test_3():
    a = [i for i in range(-45,5, 2)] + [i for i in range(100,-34, -15)] + [i for i in range(1000,340, -47)]
    e = sorted(a)
    assert recursive_sort(a) == e

