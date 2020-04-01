def format_numbers(phone_number: str) -> str:
    pn = phone_number \
        .replace('(', '') \
        .replace(')', '') \
        .replace('-', '') \
        .replace(' ', '')\
        .replace('+7', '8')
    print(pn)
    code = pn[1:4]
    three = pn[4:7]
    two_1 = pn[7:9]
    two_2 = pn[9:12]
    return f'+7({code}){three}-{two_1}-{two_2}'


phones = [
    '+7(909)111-22-33',
    '8(909)111-22-33',
    '8(909)111 22 33',
    '8(909)111 22-33',
]

for ph in phones:
    print(format_numbers(ph))
