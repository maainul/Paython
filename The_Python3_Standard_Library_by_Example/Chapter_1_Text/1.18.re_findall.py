import re

text = 'abbaaabbbbaaaaa'

pattrn = 'ba'

for match in re.findall(pattrn, text):
    print('Found {!r}'.format(match))
