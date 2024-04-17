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

    assert response == -93

def test_add_2_integers():
    num1 = -53
    num2 = 45

    response = add(num1, num2)

    assert response == -8

def test_add_2_positive_decimal_integers():
    num1 = 87.23
    num2 = 12.33

    response = add(num1, num2)

    assert response == 99.56

def test_add_2_negative_decimal_integers():
    num1 = -11.011234
    num2 = -11.01

    response = add(num1, num2)

    assert response == -22.021234

def test_add_decimal_integers():
    num1 = 111.111
    num2 = -456.563

    response = add(num1, num2)

    assert response == -345.452

def test_add_2_five_digit_positive_integers():
    num1 = 11557
    num2 = 25678

    response = add(num1, num2)

    assert response == 37235

def test_add_2_six_digit_positive_integers():
    num1 = 696969
    num2 = 420420

    response = add(num1, num2)

    assert response == 1117389

def test_add_2_Max_Positive_integers_():
    num1 = 0
    num2 = 19999999

    response = add(num1, num2)

    assert response < 20000000 

def test_add_2_Max_Negative_integers_():
    num1 = 2
    num2 = -19999999

    response = add(num1, num2)

    assert response > -20000000 


