def format_numbers(phone_number: str) -> str:
    pn = phone_number \
        .replace('(', '') \
        .replace(')', '') \
        .replace('-', '') \
        .replace(' ', '') \
        .replace('+7', '8')
    return f'+7({pn[1:4]}){pn[4:7]}-{pn[7:9]}-{pn[9:12]}'
