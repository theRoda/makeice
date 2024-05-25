import binascii

def makeSBXOR(plaintext, key):
    byteskey = bytes([key])
    bytesplain = plaintext.encode()
    encoded = bytes(x ^ y for x, y in zip(bytesplain, byteskey * len(plaintext))).decode()
    hexconvert = ''.join([str(hex(ord(c)))[2:] for c in encoded])
    return(hexconvert)