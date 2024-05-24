import string

def makeCaesar(plaintext, key):
    alphabet = string.ascii_lowercase
    shifted = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, shifted)
    encoded = plaintext.lower().translate(table)
    return(encoded)