import string

values = {'var':'foo'}

t = string.Template(""""
variable         :$var
Escape           :$$
variable in text :${var}iable
""")

print('TEMPLATES:',t.substitute(values))

s = ("""
variable         :%(var)s
Escape           :%%
variable in text :%(var)iable
""")

print('INTERPOLATION', s % values)

s = ("""
variable         :{var}
Escape           :{{}}
variable in text :{var}iable
""")

print('FORMAT:', s.format(**values))
