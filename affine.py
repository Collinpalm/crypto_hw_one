import sys
import re



#code from one of my old projects, IDK its origins
def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1


def check(text):
    dictionary = open("words.txt", "r")
    for line in dictionary:
        if (re.search(line, text)):
            print("true")
            return True
        #print(line, " ", text)
    return False
        



def decryptKey(a, b, text):
    c = modInverse(a, 26)
    newText = ""
    for i in range(0, len(text)):
        temp = (c * (text[i]+b))%26
        temp += 97
        newText += chr(temp)
    #print(newText)
    return newText




def bruteDecrypt():
    ciphertext = sys.argv[1]
    character = []
    i = 0
    print("a  b  text")
    print("__________")
    for element in range(0,len(ciphertext)):
        character.append(ord(ciphertext[element]))
        character[i] = character[i] - 97
        i = i+1
    plaintext = decryptKey(i, j, character)
    check(plaintext)
    print(i, "  ", j, "  ", plaintext, end = '\n')
    """
    for i in [1,3,5,7,9,11,15,17,19,21,23,25]:
        for j in range(0,25):
            plaintext = decryptKey(i, j, character)
            #if(check(plaintext)):
            print(i, "  ", j, "  ", plaintext, end = '\n')

"""






if __name__ == '__main__':
    bruteDecrypt()