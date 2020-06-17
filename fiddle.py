from string import ascii_uppercase


def diamond(letter, bg=' '):
    ls = ascii_uppercase[:ascii_uppercase.index(letter) + 1]
    pad = len(ls)
    if letter == ls[0]:
        return ls[0]
    elif letter == ls[1]:
        return f'{bg * (pad - 1)}{ls[0]}{bg * (pad - 1)}\n' \
               f'{ls[1]}{bg * (pad - 1)}{ls[1]}\n' \
               f'{bg * (pad - 1)}{ls[0]}{bg * (pad - 1)}\n'
    elif letter == ls[2]:
        return f'{bg * (pad - 1)}{ls[0]}{bg * (pad - 1)}\n' \
               f'{bg * (pad - 2)}{ls[1]}{bg * (pad - 2)}{ls[1]}{bg * (pad - 2)}\n' \
               f'{ls[2]}{bg * pad}{ls[2]}\n' \
               f'{bg * (pad - 2)}{ls[1]}{bg * (pad - 2)}{ls[1]}{bg * (pad - 2)}\n' \
               f'{bg * (pad - 1)}{ls[0]}{bg * (pad - 1)}\n'
    elif letter == ls[3]:
        return f'{bg * (pad - 1)}{ls[0]}{bg * (pad - 1)}\n' \
               f'{bg * (pad - 2)}{ls[1]}{bg * (pad - 3)}{ls[1]}{bg * (pad - 2)}\n' \
               f'{bg * (pad - 3)}{ls[2]}{bg * (pad - 1)}{ls[2]}{bg * (pad - 3)}\n' \
               f'{ls[3]}{bg * (pad + 1)}{ls[3]}\n' \
               f'{bg * (pad - 3)}{ls[2]}{bg * (pad - 1)}{ls[2]}{bg * (pad - 3)}\n' \
               f'{bg * (pad - 2)}{ls[1]}{bg * (pad - 3)}{ls[1]}{bg * (pad - 2)}\n' \
               f'{bg * (pad - 1)}{ls[0]}{bg * (pad - 1)}\n'
