import textwrap
from textwrap_example import sample_text
# dedent is used for removing existing indentation
dedent_text = textwrap.dedent(sample_text)
print('DEDENT:')
print(dedent_text)
