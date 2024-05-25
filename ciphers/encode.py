import string
def makeAtbash(plaintext, key):
    if key is None:
        alphabet = string.ascii_lowercase
        reversealpha = str.maketrans(alphabet, alphabet[::-1])
        encoded = plaintext.lower().translate(reversealpha)
        return(encoded)
def makeHex(plaintext, key):
    if key is None:
        encoded =  "".join([format(ord(c), '02x') for c in plaintext])
        return(encoded)


def makeReverse(plaintext, key):
    if key is None:
        encoded = plaintext[::-1]
        return(encoded)