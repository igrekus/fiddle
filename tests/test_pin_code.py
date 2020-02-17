from pyexpect import expect
from fiddle import text_to_pin_code


def test_pin_code_example():
    test = 'example test for testing {"fieldOne":1, "fields":2, "fielD":[1,"22", "e3r4"], "fieldN":"2 3 4"} more unnecessary data'
    expect(text_to_pin_code(test)).to_equal('1210')


def test_pin_code_empty_json():
    test = 'example test for testing {} more unnecessary data'
    expect(text_to_pin_code(test)).to_equal('0000')
