raw = [1, 1, 3, 4]
mx = max(raw)


def consumables(cells):
    return {(index, size): [c for c in cells if size > c] for index, size in enumerate(cells)}


can_win = list({
    k: int(v > mx)
    for k, v in {
        k[0]: sum(v) + k[1]
        for k, v in consumables(raw).items()
    }.items()
}.values())


# print(consumable)
# print(totals)
print(can_win)
