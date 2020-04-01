def format_numbers(phone_number: str) -> str:
    return ''.join([
        one.replace(' ', '') + two.replace(' ', '')
        for one, two
        in zip(
            '+7(  )  - - ',
            '  ' + ''.join([c for c in phone_number if c.isdigit()])[1:]
        )
    ])
