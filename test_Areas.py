import Areas


def test_rectanglearea():
    x = 10
    y = 20
    result = Areas.rectangleArea(x, y)
    assert x * y == result


def test_rectanglePerimeter():
    x = 20
    y = 10
    result = Areas.rectanglePerimeter(x, y)
    assert x+x+y+y == result


def test_squareArea():
    x = 5
    result = Areas.squareArea(x)
    assert x * x == result

