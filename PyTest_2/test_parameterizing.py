'''
import pytest
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
    print ("my test is passed")
'''

'''
import pytest
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 9),
    ("2+4", 7),
    ("6*9", 42),
])
def test_eval(test_input,expected):
    assert eval(test_input)+1 == expected
    print ("my test is passed")
'''


'''
import pytest

@pytest.mark.parametrize(
    'number, word', [
        (1, '1'),
        (3, 'Fizz'),
        (5, 'Buzz'),
        (10, 'Buzz'),
        (15, 'FizzBuzz'),
        (16, '16')
    ]
)
def test_fizzbuzz(number, word):
    assert fizzbuzz(number) == word

'''

'''
import pytest

@pytest.fixture(params=['apple', 'banana', 'plum'])
def fruit(request):
    return request.param

def test_is_healthy(fruit):
    assert is_healthy(fruit)

'''

'''
import pytest
@pytest.mark.parametrize(
    "number, word",
    [
        (1, "1"),
        (3, "Fizz"),
        (5, "Buzz"),
        (10, "Buzz"),
        (15, "FizzBuzz"),
        (16, "16"),
    ],
)
def test_fizzbuzz(number, word):
    assert test_fizzbuzz(number) == word
'''

'''
import pytest


@pytest.fixture(params=["apple", "banana", "plum"])
def fruit(request):
    return request.param


def test_is_healthy(fruit):
    assert test_is_healthy(fruit)
'''

'''
import pytest
@pytest.mark.parametrize("input_data,expected_data",[("1",1),("2",4),("3",9),("4",16)])
def test_addition(input_data,expected_data):
    assert (int(input_data)*int(input_data)) == expected_data
    print ("All tests are passed")
'''

'''
import pytest
@pytest.mark.parametrize("input_data,expected_data",[("1",1),("2",4),("3",9),("4",16)])
def test_addition(input_data,expected_data):
    assert (eval(input_data)*eval(input_data)) == expected_data
    print ("All tests are passed")
'''

#it doesnt work
'''
from parametrized import parametrized

import pytest
@pytest.mark.parametrize("input_data,expected_data",[("1*1",1),("2*2",4),("3*3",9),("4*4",16)])
def test_addition(input_data,expected_data):
    assert (eval(input_data)) == expected_data
    print ("All tests are passed")

@parametrized.zip
def test_addition(input_data=["1*1","2*2","3*3","4*4"],expected_result=[1,4,9,16]):
    assert eval(input_data) == expected_result
    print ("All tests are passed")
'''