def encrypt(words,n):
    result = ""
    for i in range(len(words)):
        char = words[i]
        if (char.isupper()):
            result += chr((ord(char) + n-65) % 26 + 65)
        else:
            result += chr((ord(char) + n - 97) % 26 + 97)
    return result
words = "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the government for a redress of grievances."
n = 1
print ("Input  : " + words)
print ("Shift Number : " + str(n))
print ("Cipher: " + encrypt(words,n))
