word = 'letters'
letter_count = {lette{'r': 1, 'e': 2, 'l': 1, 't': 2, 's': 1}r: word.count(letter) for letter in set(word)}
print(letter_count)

>>{'r': 1, 'e': 2, 'l': 1, 't': 2, 's': 1}

