from pyparsing import *

def  unzip(s, p, l):
    return l[0][0] * int(l[0][1:])

inp = 'Я34а4п7р15'
cyr = 'абвгдеёжзиклмнопрстувхцчшщъыьэюя'
unit = Combine(Word(alphas + cyr + cyr.upper(), exact=1) + Word(nums)).setParseAction(unzip)
string = OneOrMore(unit)

print(''.join(string.parseString(inp)))
