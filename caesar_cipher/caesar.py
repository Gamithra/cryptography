import sys

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def query():
    global ALPHABET
    print("Enter text to decrypt:")
    text = sys.stdin.readline().strip()
    print("Every letter not found in the alphabet will be printed out as-is.\n")

    print("Enter alphabet (leave empty for standard 26-letter English alphabet):")
    new_alphabet = sys.stdin.readline().strip()
    if new_alphabet != "":
        ALPHABET = new_alphabet
        print("New alphabet is " + ALPHABET)
    print("")

    print("Enter shift (leave empty for all 26 possibilities):")
    shift = sys.stdin.readline().strip()
    print("")
    if shift == "":
        decrypt_all(text)
    else:
        decrypt(text, int(shift))

def decrypt_all(text):
    for i in range(len(ALPHABET)):
        decrypt(text, i)

def decrypt(text, shift):
    print("Result for shift " + str(shift) + ":")
    result = ""
    for i in range(len(text)):
        uppercase = text[i].isupper()
        if text[i].lower() in ALPHABET:
            letter = ALPHABET[(ALPHABET.index(text[i].lower())-shift+len(ALPHABET))%len(ALPHABET)]
            if uppercase:
                result += letter.upper()
            else:
                result += letter
        else:
            result += text[i]
    print(result)

query()
