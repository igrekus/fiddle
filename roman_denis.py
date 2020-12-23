roman_numbers = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
                 10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
                 100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
                 1000: "M", 2000: "MM", 3000: "MMM"}
arabian_numbers = {value: key for key, value in roman_numbers.items()}


def to_roman(n: int) -> str:
    thousands, hundreds, dozens, units = list(map(int, list(str(n).rjust(4, "0"))))
    roman_thousands = roman_numbers[thousands * 1000]
    roman_hundreds = roman_numbers[hundreds * 100]
    roman_dozens = roman_numbers[dozens * 10]
    roman_units = roman_numbers[units]
    return roman_thousands + roman_hundreds + roman_dozens + roman_units


def parse_roman(roman: str) -> int:
    if not roman:
        return -1
    for char in set(roman):
        if char * 4 in roman:
            return -1

    def parser(roman_num: str, num_range: list) -> tuple:
        number = 0
        best_key = ""
        for key in arabian_numbers:
            if roman_num.endswith(key) and len(key) > len(best_key):
                best_key = key
                number = arabian_numbers.get(key, 0)
        if number not in num_range:
            best_key = ""
            number = 0
        return number, best_key

    parsed = False
    units, used_key = parser(roman, list(range(1, 10, 1)))
    dozens, used_key = parser(roman := roman.replace(used_key, "", 1), list(range(10, 100, 10)))
    hundreds, used_key = parser(roman := roman.replace(used_key, "", 1), list(range(100, 1000, 100)))
    thousands, used_key = parser(roman := roman.replace(used_key, "", 1), list(range(1000, 3001, 1000)))
    roman = roman.replace(used_key, "", 1)
    if roman == "":
        parsed = True
    return thousands + hundreds + dozens + units if parsed else -1
