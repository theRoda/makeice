import ciphers as c

test = 'This is a plaintext string.'
def main():
    ice = c.makeCaesar(test, 13)
    print(ice)

if __name__ == "__main__":
	main()