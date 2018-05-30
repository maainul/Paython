import re
phone=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phone.search('My phone number is 412-444-9870')
print(mo.group(1))
print(mo.group(2))
print(mo.group())

"""
Output:

412
444-9870
412-444-9870
"""
