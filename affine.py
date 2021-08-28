import sys
import re



#code from one of my old projects, IDK its origins
def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1


def check(text):
    if():
        return True
    return False
        



def decryptKey(a, b, text):
    c = modInverse(a, 26)
    newText = ""
    for i in range(0, len(text)):
        temp = (c * (text[i]+b))%26
        newText += chr(temp)
    return newText




def bruteDecrypt():
    ciphertext = sys.argv[1]
    character = [0]
    i = 0
    print("a  b  text\n")
    print("__________")
    for element in range(0,len(ciphertext)):
        character[i] = ord(ciphertext[element])
        character[i] = character - 65
        i = i+1
    for i in [1,3,5,7,9,11,15,17,19,21,23,25]:
        for j in range(0,25):
            plaintext = decryptKey(i, j, character)
            if(check(plaintext)):
                print(i, "  ", j, "  ", plaintext, end = '\n')








if __name__ == '__main__':
    bruteDecrypt()