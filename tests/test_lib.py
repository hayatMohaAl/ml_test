# tests/test_lib.py
from ml_test.lib import hello_world

def test_length_of_hello_world():
    assert len(hello_world()) != 0
