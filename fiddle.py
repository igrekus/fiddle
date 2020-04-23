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
            return '''2 бутылки пива на стене, 2 бутылки пива!
Возьми одну, передай мне, 1 бутылка пива на стене
'''
        elif num == 89:
            return '''89 бутылок пива на стене, 89 бутылок пива!
Возьми одну, передай мне, 88 бутылок пива на стене
'''
        elif num == 98:
            return f'''{num} бутылок пива на стене, {num} бутылок пива!
Возьми одну, передай мне, {num - 1} бутылок пива на стене
'''
        elif num == 99:
            return f'''{num} бутылок пива на стене, {num} бутылок пива!
Возьми одну, передай мне, {num - 1} бутылок пива на стене
'''
        else:
            return ''

    def verses(self, upper, lower):
        return '\n'.join([self.verse(num) for num in reversed(range(lower, upper + 1))])

    @property
    def song(self):
        return self.verses(99, 0)
