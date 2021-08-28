import sys

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def encrypt():
    plaintext = sys.argv[1]
    a = sys.argv[2]
    b = sys.argv[3]
    character = []
    cipherText = ""
    for element in range(0,len(plaintext)):
        character.append(ord(plaintext[element]))
        character[i] = character[i] - 97
        character[i] = ((a * character[i]) + b) % 26
        character[i] = character[i] + 97
        character[i] = chr(character[i])
        i = i+1
    for i in range(0, len(character)):
        cipherText += character[i]

    print("Encrypted Text")
    print(cipherText)





    
if __name__ == '__main__':
    encrypt()