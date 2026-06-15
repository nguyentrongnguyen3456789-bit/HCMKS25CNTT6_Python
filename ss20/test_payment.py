from main import calculate_payment
import pytest

# trường hợp tốt nhất
def test_happy():
    assert calculate_payment(100.0, 0.1) == 90.0

def test_full_rate():
    assert calculate_payment(100.0, 1) == 0.0

def test_zero_rate():
    assert calculate_payment(100.0, 0.0) == 100.0

# trường hợp xấu nhất
def test_zero_rate():
    with pytest.raises(ValueError):
        calculate_payment(150.0, 0.0)
