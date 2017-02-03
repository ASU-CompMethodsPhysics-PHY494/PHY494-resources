from mean import mean

import pytest

def test_ints():
    num_list = [1, 2, 3, 4, 5]
    obs = mean(num_list)

    assert obs == 3

def test_not_numbers():
    values = [2, "lolcats"]
    with pytest.raises(TypeError):
        out = mean(values)

def test_zero():
    num_list = [0, 2, 4, 6]
    assert mean(num_list) == 3

def test_empty():
    assert mean([]) == 0

def test_single_int():
    with pytest.raises(TypeError):
        mean(1)

