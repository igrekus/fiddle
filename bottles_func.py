qty = {0: 'нет', 1: 'последняя', -1: '99'}
bottle = {
    **dict.fromkeys([1] + list(range(21, 92, 10)), 'бутылка'),
    **dict.fromkeys(
        [o + 10 * int(d) for o, d in zip([2, 3, 4] * 10, [i for i in '023456789' for _ in 'rep'])],
        'бутылки'
    )
}


def song() -> str:
    return verses(99, 0)


def verses(upper: int, lower: int) -> str:
    return '\n'.join(
        '{0} {1} пива на стене, {2} {1} пива!\n{3}, {4} {5} пива на стене.\n'
        .format(
            qty.get(num, f'{num}').capitalize(),
            bottle.get(num, 'бутылок'),
            qty.get(num, f'{num}'),
            {0: 'Сходи в магазин, купи ещё'}.get(num, f'Возьми {dict([(1, "её")]).get(num, "одну")}, передай мне'),
            qty.get(num - 1, f'{num - 1}'),
            bottle.get(num - 1, 'бутылок')
        )
        for num in range(upper, lower - 1, -1)
    )
