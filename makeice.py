import string

import ciphers as c

icebox = []

test = 'This is a plaintext string.'

text5 = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key5 = "ICE"

def iceAll(plaintext, key):
    caesar = c.makeCaesar(plaintext, key)
    atbash = c.makeAtbash(plaintext, key)
    sbxor = c.makeSBXOR(plaintext, key)
    rkxor = c.makeRKXOR(plaintext, key)
    icebox.append(f'[!] {caesar} | CAESAR | {key}')
    icebox.append(f'[!] {atbash} | ATBASH | {key}')
    icebox.append(f'[!] {sbxor} | SBXOR | {key}')
    icebox.append(f'[!] {rkxor} | RKXOR | {key}')
    for ciph in icebox:
        print(ciph)

def main():
    iceAll(text5, key5)

if __name__ == "__main__":
    main()