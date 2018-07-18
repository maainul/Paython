import re

address = re.compile(
   ''' 
    [\w\d.+-]+      # username
    @
    ([\w\d.]+\.)+   # domain name prefix
    (com|org|edu)   #TODO: support more top-level domains
    ''',
    re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid.address@gmail.example.com',
    u'not-valid@example.so',
    u'mainul080@gmail.com',
    u'mainul_hasan@gmail.com',
    u'mainul+hasan3787@gmail.com'
]

for candidate in candidates:
    match = address.search(candidate)
    print('{:<40} {}'.format(candidate, 'Match' if match else 'No Match'))
