def max_common_string(first_string: str, second_string: str) -> str:
    if not first_string or not second_string:
        return ""
    f, fs, s, ss = first_string[0], first_string[1:], second_string[0], second_string[1:]
    return \
        f + max_common_string(fs, ss) if f == s else \
        max(max_common_string(first_string, ss), max_common_string(fs, second_string), key=len)
