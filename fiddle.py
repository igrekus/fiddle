from string import ascii_uppercase


def diamond(letter, background=' '):
    letters = ascii_uppercase[:ascii_uppercase.index(letter) + 1]
    if letter == letters[0]:
        return letters[0]
    elif letter == letters[1]:
        return f' {letters[0]} \n' \
               f'{letters[1]} {letters[1]}\n' \
               f' {letters[0]} \n'
    elif letter == letters[2]:
        return f'  {letters[0]}  \n' \
               f' {letters[1]} {letters[1]} \n' \
               f'{letters[2]}   {letters[2]}\n' \
               f' {letters[1]} {letters[1]} \n' \
               f'  {letters[0]}  \n'
    elif letter == letters[3]:
        return f'   {letters[0]}   \n' \
               f'  {letters[1]} {letters[1]}  \n' \
               f' {letters[2]}   {letters[2]} \n' \
               f'{letters[3]}     {letters[3]}\n' \
               f' {letters[2]}   {letters[2]} \n' \
               f'  {letters[1]} {letters[1]}  \n' \
               f'   {letters[0]}   \n'
