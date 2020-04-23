class Bottles:
    def verse(self, num):
        if num == 0:
            return '''Нет бутылок пива на стене, нет бутылок пива!
Сходи в магазин, купи ещё, 99 бутылок пива на стене
'''
        elif num == 1:
            return '''1 бутылка пива на стене, 1 бутылка пива!
Возьми одну, передай мне, нет бутылок пива на стене
'''
        elif num == 2:
            return f'''{num} бутылки пива на стене, {num} бутылки пива!
Возьми одну, передай мне, {num - 1} бутылка пива на стене
'''
        else:
            return f'''{num} бутылок пива на стене, {num} бутылок пива!
Возьми одну, передай мне, {num - 1} бутылок пива на стене
'''

    def verses(self, upper, lower):
        return '\n'.join(filter(bool, [self.verse(num) for num in reversed(range(lower, upper + 1))]))

    @property
    def song(self):
        return self.verses(99, 0)
