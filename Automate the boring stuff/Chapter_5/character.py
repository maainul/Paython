message='It is a bright cold day in April,and the clocks were striking thirteen.'
count={}
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1
print(count)

#
{'I': 1, 't': 6, ' ': 12, 'i': 7, 's': 3, 'a': 3, 'b': 1, 'r': 5, 'g': 2, 'h': 3, 'c': 3, 'o': 2, 'l': 3, 'd': 3, 'y': 1, 'n': 4, 'A': 1, 'p': 1, ',': 1, 'e': 5, 'k': 2, 'w': 1, '.': 1}
#

import pprint
message='It is a bright cold day in April,and the clocks were striking thirteen.'
count={}
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1
pprint.pprint(count)
#
{' ': 12,
 ',': 1,
 '.': 1,
 'A': 1,
 'I': 1,
 'a': 3,
 'b': 1,
 'c': 3,
 'd': 3,
 'e': 5,
 'g': 2,
 'h': 3,
 'i': 7,
 'k': 2,
 'l': 3,
 'n': 4,
 'o': 2,
 'p': 1,
 'r': 5,
 's': 3,
 't': 6,
 'w': 1,
 'y': 1}
