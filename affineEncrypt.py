import sys

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def encrypt():
    ciphertext = sys.argv[1]
    character = []
    for element in range(0,len(ciphertext)):
        character.append(ord(ciphertext[element]))
        character[i] = character[i] - 97
        i = i+1
    
    





    
if __name__ == '__main__':
    encrypt()