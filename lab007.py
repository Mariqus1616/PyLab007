alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
alpha_len = len(alphabet)

def pretty_print(vsq: list):
    for i, row in enumerate(vsq):
        print(f"| {' | '.join(row)} |")
        if i == 0:

            suffix = '___|'* (alpha_len + 1)
            print(f'|{suffix}|')


def print_header():
    header = [' ']
   #print('|   |', end='')
    for a in alphabet:
        header.append(a)
        #print(f' {a} |', end='')
    #print()
    #suffix = '---|' * (alpha_len + 1)
    #print(f'|{suffix}')
    return header

def print_row(a:int):
    row = []
    for c in range(alpha_len):
        row.append(alphabet[(c + a) % alpha_len])
    return row

    #print(f' {alphabet[(c+a) % alpha_len]} |', end='')
    print()
    return row

def vigenere_sq():
    sq = []
    sq.append(print_header())
    for a in range(alpha_len):
        #print(f'| {alphabet[a]} |', end='')
        row = print_row(a)
        row.insert(0, alphabet[a])
        sq.append(row)
    return sq

pretty_print( vigenere_sq() )

def letter_to_index(letter:str, alphabet:str):
    for i,c in enumerate (alphabet):
        if letter == c:
            return i
    return -1

def index_to_letter(index:int, alphabet:str):
    if 0 <=index < alpha_len:
        return alphabet[index]
    return None

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    pi = ((letter_to_index(cipher_letter,alphabet) -
           letter_to_index(key_letter,alphabet)) % alpha_len)
    return index_to_letter(pi, alphabet)

def vigenere_index(key_letter, plaintext_letter, alphabet):
    ci = ((letter_to_index(key_letter,alphabet) +
           letter_to_index(plaintext_letter,alphabet)) % alpha_len)
    print(ci)
    return index_to_letter(ci, alphabet)

def encrypt_vigeneren(key, plaintext, alphabet):
    cipher_text = []
    for i, pt in enumerate(plaintext):
        #print
        cipher_text.append(vigenere_index(key[i%len(key)], pt, alphabet))
    return ''.join(cipher_text)

def decrypt_vigeneren(key, ciphertext, alphabet):
    plain_text = []
    for i, pt in enumerate(ciphertext):
        plain_text.append(undo_vigenere_index(key[i%len(key)], pt, alphabet))
    return ''.join(plain_text)



#vigenere_sq()
#print(letter_to_index('Z', alphabet))
#print(letter_to_letter(27,alphabet))
key = 'DAVINCI'
plaintext = 'THE EAGLE HAS LANDED'

#print(vigenere_index( 'D', 'T' , alphabet))
ct = encrypt_vigeneren(key, plaintext, alphabet)
pt = decrypt_vigeneren(key, ct, alphabet)

while True:
    choice = int(input())
    if 1 <= choice <= 3:
        break

