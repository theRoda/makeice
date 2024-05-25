

def makeHex(plaintext, key):
    if key is None:
        encoded =  "".join([format(ord(c), '02x') for c in plaintext])
        return(encoded)
