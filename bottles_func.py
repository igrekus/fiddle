def song():
    return verses(99, 0)


def verses(upper, lower):
    return '\n'.join(_verse(n) for n in range(upper, lower - 1, -1))


def _verse(num):
    return (
        f'{_quantity(num).capitalize()} {_container(num)} пива на стене, '
        f'{_quantity(num)} {_container(num)} пива!\n'
        f'{_action(num)}, '
        f'{_quantity(num - 1)} {_container(num - 1)} пива на стене.\n'
    )

def _action(num):
    return {0: 'Сходи в магазин, купи ещё'}.get(num, f'Возьми {dict([(1, "её")]).get(num, "одну")}, передай мне')

def _quantity(num):
    return {0: 'нет', 1: 'последняя', -1: '99'}.get(num, f'{num}')

def _container(num):
    return {
        **dict.fromkeys([1] + list(range(21, 92, 10)), 'бутылка'),
        **dict.fromkeys(
            [o + 10 * int(d) for o, d in zip(
                [2, 3, 4] * 10,
                [i for i in '023456789' for _ in 'rep'])],
            'бутылки'
        )
    }.get(num, 'бутылок')
