import re
phone=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phone.search('My phone number is 412-444-9870')
print(mo.group())
"""
OUTPUT:
412-444-9870
"""
