import textwrap
from textwrap_example import sample_text

def should_indent(line):
    print('Indent {!r}?'.format(line))
    return len(line.strip()) %2 == 0

dedent_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedent_text,width=50)
final = textwrap.indent(wrapped,'Even ',predicate=should_indent)

print('\nQuoted block:\n')
print(final)
