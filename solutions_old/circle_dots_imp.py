def count_dots(radius):
    return sum(2 * int((radius ** 2 - x ** 2) ** 0.5) + 1 for x in range(-int(radius), int(radius) + 1))
