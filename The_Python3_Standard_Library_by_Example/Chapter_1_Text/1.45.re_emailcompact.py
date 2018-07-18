import re

address = re.compile('[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)')

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid.address@gmail.example.com',
    u'not-valid@example.so'
]

for candidate in candidates:
    match = address.search(candidate)
    print('{:<40} {}'.format(candidate, 'Match' if match else 'No Match'))
