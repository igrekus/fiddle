class rpartial:
    def __new__(cls, func, *args, **keywords):
        self = super().__new__(cls)
        self.func = func
        self.args = args
        self.keywords = keywords
        return self
    def __call__(self, *args, **kwargs):
        kw = self.keywords.copy()
        kw.update(kwargs)
        return self.func(*(args + self.args), **kw)


old = list('()- ') + ['+7']
new = [''] * 4 + ['8']


def format_numbers(phone_number: str) -> str:
    for f in [rpartial(str.replace, o, n) for o, n in zip(old, new)]:
        phone_number = f(phone_number)
    code = phone_number[1:4]
    three = phone_number[4:7]
    two_1 = phone_number[7:9]
    two_2 = phone_number[9:12]
    return f'+7({code}){three}-{two_1}-{two_2}'


phones = [
    '+7(909)111-22-33',
    '8(909)111-22-33',
    '8(909)111 22 33',
    '8(909)111 22-33',
]

for ph in phones:
    print('out:', format_numbers(ph))
