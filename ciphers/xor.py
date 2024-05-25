def makeSBXOR(plaintext, key):
    if isinstance(key, int) and key < 256:
        byteskey = bytes([key])
        bytesplain = plaintext.encode()
        encoded = bytes(x ^ y for x, y in zip(bytesplain, byteskey * len(plaintext))).decode()
        hexconvert = ''.join([str(hex(ord(c)))[2:] for c in encoded])
        return(hexconvert)

def makeRKXOR(plaintext, key):
    if isinstance(key, str):
        bytesplain = bytearray.fromhex(plaintext.encode().hex())
        byteskey = bytearray.fromhex(key.encode().hex())
        encrypted = [bytestr ^ byteskey[index % len(byteskey)] for index, bytestr in enumerate(bytesplain)]
        hexencoded = ''.join(["%02x" % ord(chr(x)) for x in encrypted])
        return(hexencoded)