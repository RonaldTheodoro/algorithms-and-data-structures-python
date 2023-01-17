from src.stack_decimal_to_binary import decimal_to_binary


def test_decimal_to_binary():
    assert decimal_to_binary(233) == "11101001"
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(1000) == "1111101000"
