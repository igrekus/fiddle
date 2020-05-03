def _recur(it, d):
    """
    Helper
    """
    if d == -1:
        yield it
    else:
        for i in it:
            if isinstance(i, list):
                yield from _recur(i, d - 1)
            else:
                yield i


def flatten(a_list: list, depth: int=0) -> list:
    """
    Public API
    """
    return list(_recur(a_list, depth if depth else float('inf')))
