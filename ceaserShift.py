ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def main(ciphertext):
    for key in range(0, len(ALPHABET)):
        for element in ciphertext:
            character = ord(element)
            character = character - 64
            character = (character + key) % 26
            print(chr(character))
            character = ''
        print("\n")
