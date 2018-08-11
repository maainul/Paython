import datetime
print('Now:',datetime.datetime.now())
FIELDS =[
    'year','month','day','hour','minute','second','microsecond',
]
d=datetime.datetime.now()
for attr in FIELDS:
    print('{}:{}'.format(attr,getattr(d,attr)))
