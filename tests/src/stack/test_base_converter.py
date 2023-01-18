from src.stack_base_converter import base_converter


def test_base_converter():
    assert base_converter(100345, 2) == "11000011111111001"
    assert base_converter(100345, 8) == "303771"
    assert base_converter(100345, 16) == "187F9"
    assert base_converter(100345, 35) == "2BW0"
    assert base_converter(100345, 40) == ""
