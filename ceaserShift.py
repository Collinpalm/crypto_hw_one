import sys

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def bruteDecrypt():
    ciphertext = sys.argv[1]
    for key in range(0, len(ALPHABET)):
        for element in range(0,len(ciphertext)):
            character = ord(ciphertext[element])
            character = character - 64
            character = (character + key) % 26
            character = character + 64
            temp = chr(character)
            print(temp)
    print("\n")

if __name__ == '__main__':
    bruteDecrypt()