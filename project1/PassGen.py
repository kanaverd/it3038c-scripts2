import random

def generatePassword(p):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%"

    chosenLetter = random.sample(characters, p)
    password ="".join(chosenLetter)
    return password

if __name__== "__main__":
    p = int(input("Please enter the desired length of the password: "))
    password = generatePassword(p)
    print("The password is:", password)
