from scripts.calculator import add


def test_add_zero():
    num1 = 0
    num2 = 0

    response = add(num1, num2)

    assert response == 0

def test_add_2_positive_integers():
    num1 = 572
    num2 = 17

    response = add(num1, num2)

    assert response == 589

def test_add_2_negative_integers():
    num1 = -3
    num2 = -90

    response = add(num1, num2)

    assert response == -92