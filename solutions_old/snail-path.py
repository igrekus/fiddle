# from coconut.convenience import *
#
# inp = ".>>>VV<<V"
#
# coconut_eval('"hi" |> print')
#
#


def run(move):
    pass


char, *path = '@VVVV>>>>>>>>>>V<<VVVV<<<VV>>>'
lines = ''.join(path).split('V')
outp = ''

spaces = 0
for line in lines:
    if '<' in line:
        spaces -= len(line)

    outp += ' ' * spaces + char * (len(line) + 1) + '\n'

    if '>' in line:
        spaces += len(line)

print(outp)
