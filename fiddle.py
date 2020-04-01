def format_numbers(phone_number: str) -> str:
    return ''.join([
        one.replace(' ', '') + two.replace(' ', '')
        for one, two
        in zip(
            '+7(  )  - - ',
            '  ' + ''.join([c for c in phone_number if c.isdigit()])[1:]
        )
    ])


phones = [
    '+7(909)111-22-33',
    '8(909)111-22-33',
    '8(909)111 22 33',
    '8(909)111 22-33',
]

for ph in phones:
    print('out:', format_numbers(ph))
