'''
Write a Python function to convert a given string to all
uppercase if it contains at least 2 uppercase characters
in the first 4 characters.
'''

def stringToUpper(UserInput):
    parseLimit = 4
    upperCharCount = 0
    for letter in UserInput:
        if letter.isupper():
            upperCharCount += 1
        if upperCharCount >= 2:
            return UserInput.upper()
        parseLimit -= 1
        if parseLimit == 0:
            break
    return "Does not meet requirement"

userInput = input("Enter string: ")
print("Output: " + stringToUpper(userInput))





