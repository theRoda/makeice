import string

def makeAtbash(plaintext, key):
    alphabet = string.ascii_lowercase
    reversealpha = str.maketrans(alphabet, alphabet[::-1])
    encoded = plaintext.lower().translate(reversealpha)
    return(encoded)