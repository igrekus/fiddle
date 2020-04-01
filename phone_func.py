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


def format_numbers(phone_number: str) -> str:
    for f in [rpartial(str.replace, o, n) for o, n in zip(list('()- ') + ['+7'], [''] * 4 + ['8'])]:
        phone_number = f(phone_number)
    return f'+7({phone_number[1:4]}){phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:12]}'
