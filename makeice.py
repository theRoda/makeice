import argparse
import ciphers as c

parser = argparse.ArgumentParser(description='this encrypts')
plainmethod = parser.add_mutually_exclusive_group()
plainmethod.add_argument('-p', '--plaintext', type=str, default=None, help='Give plaintext as an argument.')
plainmethod.add_argument('-f', '--file', type=str, default=None, help='Give plaintext as a file.')
keymethod = parser.add_mutually_exclusive_group()
keymethod.add_argument('-i', '--intkey', default=None, type=int, help='Give integer key as an argument.')
keymethod.add_argument('-s', '--strkey', default=None, type=str, help='Give string key as an argument.')

icebox = []

test = 'This is a plaintext string.'

text5 = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key5 = "ICE"

def iceAll(plaintext, key):
    print(f'[!] Using plaintext: {plaintext}')
    print(f'[!] Using key: {key}')
    caesar = c.makeCaesar(plaintext, key)
    atbash = c.makeAtbash(plaintext, key)
    sbxor = c.makeSBXOR(plaintext, key)
    rkxor = c.makeRKXOR(plaintext, key)
    encodehex = c.makeHex(plaintext, key)
    reverse = c.makeReverse(plaintext, key)
    b64 = c.makeBase64(plaintext, key)
    icebox.append(f'[!] {caesar} | CAESAR | {key}')
    icebox.append(f'[!] {atbash} | ATBASH | {key}')
    icebox.append(f'[!] {sbxor} | SBXOR | {key}')
    icebox.append(f'[!] {rkxor} | RKXOR | {key}')
    icebox.append(f'[!] {encodehex} | HEX | {key}')
    icebox.append(f'[!] {reverse} | REVERSE | {key}')
    icebox.append(f'[!] {b64} | BASE64 | {key}')
    for ciph in icebox:
        print(ciph)

def main():
    args = parser.parse_args()
    if args.intkey is not None:
        key = args.intkey
    elif args.strkey is not None:
        key = args.strkey
    else:
        key = None

    if args.plaintext is not None:
        plaintext = args.plaintext
        iceAll(plaintext, key)
    elif args.file is not None:
        plainfile = args.file
        with open(plainfile, 'r') as filename:
            plaintext = filename.read()
            iceAll(plaintext, key)
    else:
        plaintext = test
        key = "ICE"
        print(f'[!] No plaintext provided. Encrypting a plaintext anyway.')
        iceAll(plaintext, key)


if __name__ == "__main__":
    main()