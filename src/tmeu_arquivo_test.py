def test_something():
    v = ["cachorro", "gato"]
    assert "gato" in v


def test_something2():
    x = 3
    isTrue = None

    if x < 2:
        isTrue = True

    assert isTrue is not True
