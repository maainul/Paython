import textwrap
from textwrap_example import sample_text

dedent_text = textwrap.dedent(sample_text).strip()

for width in [45,60]:
    print('{}Column:\n'.format(width))
    print(textwrap.fill(dedent_text,width=width))
    print()

