from pyexpect import expect
from fiddle import text_to_pin_code


def test_pin_code_example():
    test = 'example test for testing {"fieldOne":1, "fields":2, "fielD":[1,"22", "e3r4"], "fieldN":"2 3 4"} more unnecessary data'
    expect(text_to_pin_code(test)).to_equal('1210')


def test_pin_code_empty_json():
    test = 'example test for testing {} more unnecessary data'
    expect(text_to_pin_code(test)).to_equal('0000')


def test_pin_code_empty_input_string():
    test = '{}'
    expect(text_to_pin_code(test)).to_equal('0000')


def test_pin_code_empty_strings_in_list_field():
    test = 'example test for testing {"fieldOne":1, "fielDs":2, "fielD":[5, "a", "ebc"], "fieldn":"2 3 4"} more unnecessary data'
    expect(text_to_pin_code(test)).to_equal('3000')


def test_pin_code_non_num_string_in_string_field():
    test = 'example test for testing {"fieldOne":1, "fielDs":2, "fielD":[5, "a", "ebc"], "fieldN":"aaa"} more unnecessary data'
    expect(text_to_pin_code(test)).to_equal('3000')


def test_pin_code_only_ones():
    test = 'example test for testing {"fieldOne":1, "fielDs":2, "fielD":[5, "a", "ebc"], "fieldN":"aaa"} more unnecessary data'
    expect(text_to_pin_code(test)).to_equal('3000')


def test_pin_code_only_twoes():
    test = 'example test for testing {"fieldone":1, "fields":2, "fielD":[25, "22", "e45c"], "fieldn":"aaa"} more unnecessary data'
    expect(text_to_pin_code(test)).to_equal('0300')


def test_pin_code_only_threes():
    test = 'example test for testing {"fieldOne":122, "fields":2, "fielD":[333, "jj", ""], "fieldN":"999"} more unnecessary data'
    expect(text_to_pin_code(test)).to_equal('0030')


def test_pin_code_only_fours():
    test = 'example test for testing {"fieldOne":1222, "fields":2, "fielD":["gggg", "jj", ""], "fieldn":"999"} more unnecessary data'
    expect(text_to_pin_code(test)).to_equal('0001')


def test_pin_code_bool_in_list():
    test = 'example test for testing {"fieldOne":4, "fields":2, "fielD":[5, "22", "e3r4", true], "fieldN":"2 3 4"} more unnecessary data'
    expect(text_to_pin_code(test)).to_equal('2210')

