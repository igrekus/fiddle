class Bottles:
    def verse(self, num):
        if num == 0:
            return '''Нет бутылок пива на стене
Нет бутылок пива!
Сходи в магазин, купи ещё
99 бутылок пива на стене
'''
        elif num == 1:
            return '''1 бутылка пива на стене
1 бутылка пива!
Возьми одну, передай мне
Нет бутылок пива на стене
'''
        elif num == 2:
            return '''2 бутылки пива на стене
2 бутылки пива!
Возьми одну, передай мне
1 бутылка пива на стене
'''
        elif num == 99:
            return '''99 бутылок пива на стене
99 бутылок пива!
Возьми одну, передай мне
98 бутылок пива на стене
'''
        elif num == 89:
            return '''89 бутылок пива на стене
89 бутылок пива!
Возьми одну, передай мне
88 бутылок пива на стене
'''
