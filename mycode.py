def encrypt(words,n):
    count_1 = 0
    count_2 = 0
    result = ""
    test = ""
    ten = "Cipher:"
    new_list = []
    for i in range(len(words)):
        char = words[i]
        if (char.isupper()):
            result += chr((ord(char) + n-65) % 26 + 65)
        else:
            result += chr((ord(char) + n - 97) % 26 + 97)
    
    for i in result:
      if count_1 < 5:
        test = test + i
        count_1 += 1
      else:
        new_list.append(test.upper())
        test = ""
        count_1 = 1
        test = i
    new_list.append(test.upper())

    for i in new_list:
      if count_2 < 10:
        ten = ten + " " + i
        count_2 += 1
      else:
        print(ten)
        count_2 = 1
        ten = ""
        ten = i
    print(ten)


words = "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the government for a redress of grievances."
n = 1
print ("Input  : " + words)
print ("Shift Number : " + str(n))
(encrypt(words,n))
