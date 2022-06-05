def palindrome(word, s, e):
    #only 1 character length - direct palindrome
    if(s==e):
        return True
    if(word[s] != word[e]):
        return False
    else:
        return palindrome(word, s+1, e-1)

word = "malayalam"
wordLen = len(word)
print(palindrome(word, 0, wordLen-1))