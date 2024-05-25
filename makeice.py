import string

import ciphers as c

icebox = []

test = 'This is a plaintext string.'

text5 = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key5 = "ICE"

def iceAll(plaintext, key):
    caesar = c.makeCaesar(test, key)
    atbash = c.makeAtbash(test, key)
    sbxor = c.makeSBXOR(test, key)
    if caesar is not None:
        icebox.append(f'[!] {caesar} | CAESAR | {key}')
    else:
        icebox.append(f'[!] {caesar} | CAESAR | {key}')
    icebox.append(f'[!] {atbash} | ATBASH | N/A')
    icebox.append(f'[!] {sbxor} | SBXOR | {key}')
    for ciph in icebox:
        print(ciph)

def main():
    iceAll(test, key5)

if __name__ == "__main__":
    main()