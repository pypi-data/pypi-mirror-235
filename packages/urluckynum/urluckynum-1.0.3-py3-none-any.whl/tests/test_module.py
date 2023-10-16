import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src") 

from app.lucky import generate_lucky_number

@pytest.mark.unit
def test_generate_lucky_number():
    # test the generate_lucky_number function
    result = generate_lucky_number()
    assert isinstance(result, int), "Expected an integer result"
    assert 0 <= result <= 42, "Lucky number should be between 0 and 42"