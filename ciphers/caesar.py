import string

def makeCaesar(plaintext, key):
    if isinstance(key, int) and key < 26:
        alphabet = string.ascii_lowercase
        shifted = alphabet[key:] + alphabet[:key]
        caesaralpha = str.maketrans(alphabet, shifted)
        encoded = plaintext.lower().translate(caesaralpha)
        return(encoded)