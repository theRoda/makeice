import string

def makeAtbash(plaintext, key):
    if key is None:
        alphabet = string.ascii_lowercase
        reversealpha = str.maketrans(alphabet, alphabet[::-1])
        encoded = plaintext.lower().translate(reversealpha)
        return(encoded)