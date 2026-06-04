import pytest

def square(n):
    return n**2
def cube(n):
    return n**3
def fifth(n):
    return n**5
def test_square():
    assert square(2) == 4, "Test Failed :  Square of  2 is equal to 4"
    assert square(3) == 9, "Test Failed : Square of 3 is equal to 9"
def test_cube():
    assert cube(2) == 8, "Test Failed :  Cube of  2 is equal to 8"
    assert cube(3) == 27, "Test Failed : Cube of 3 is equal to 27"
def test_fifth():
    assert fifth(2) == 32, "Test Failed :  Fifth Power of  2 is equal to 32"
    assert fifth(3) == 243, "Test Failed : Fifth Power of 3 is equal to 243"
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")