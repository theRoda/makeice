import string

def makeCaesar(plaintext, key):
    if isinstance(key, int):
        alphabet = string.ascii_lowercase
        shifted = alphabet[key:] + alphabet[:key]
        table = str.maketrans(alphabet, shifted)
        encoded = plaintext.lower().translate(table)
        return(encoded)