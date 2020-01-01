from sample import say_hello
import pytest
from mock import patch, Mock


def test_say_hello_success():
    r_greet = say_hello('sample_name')
    assert r_greet == 'Hello mr sample_name !'
    with pytest.raises(Exception, match = 'Can not greet to invisible !'):
        say_hello()