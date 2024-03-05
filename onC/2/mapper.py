def letterToIndex(letter):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    idx = alphabet.find(letter)
    if idx == -1: #not found
        print(f'Error: {letter} not found in {alphabet}')
    return idx

def indexToLetter(idx):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    letter = ''
    if idx >= len(alphabet):
        print(f'Error: {idx} not found in {alphabet}')
    elif idx < 0:
        print(f'Error: {idx} not found in {alphabet}')
    else:
        letter = alphabet[idx]
    return letter