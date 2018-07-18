import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
original = textwrap.fill(dedented_text,width=50)

print('Original:')
print(original)

shortend = textwrap.shorten(original,100)
shoretend_wrapped = textwrap.fill(shortend,width=50)

print('\nShortened:')
print(shoretend_wrapped)
