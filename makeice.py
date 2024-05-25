import string

import ciphers as c

icebox = []

test = 'This is a plaintext string.'

def iceAll(plaintext, key):
    caesar = c.makeCaesar(test, key)
    atbash = c.makeAtbash(test, key)
    sbxor = c.makeSBXOR(test, key)
    icebox.append(f'[!] {caesar} | CAESAR | {key}')
    icebox.append(f'[!] {atbash} | ATBASH | N/A')
    icebox.append(f'[!] {sbxor} | SBXOR | {key}')
    for ciph in icebox:
        print(ciph)

def main():
    iceAll(test, 13)

if __name__ == "__main__":
    main()