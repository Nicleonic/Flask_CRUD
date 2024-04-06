# import math as m

# def rsa(plainText,n,e):
#     cipherText  = []
#     codeChart = "abcdefghijklmnopqrstuvwxyz"

#     for key in codeChart:
#         for i in plainText:
#             if key == i:
#                 char = codeChart.index(key)
#                 # print(char)
#                 c = int(m.pow(char, e) % n)
#                 # print(c)
#                 cipherText.append(c)
#     return cipherText


# def dechRSA(messageChiffre,d,n):
#     plainText = ""
#     codeChart = "abcdefghijklmnopqrstuvwxyz"
#     for i in messageChiffre:
#         # plainText += str(m.pow(i,d)%n)
#         char = m.pow(i,d)%n
#         for key in range(len(codeChart)):
#             if key == char:
#                 plainText += codeChart[key]
#     return plainText



# message = "hib"

# print(rsa(message, 33, 3))
# # print(" -----------Dechiffrement--------")

# cipherText = [1, 13, 17]

# # print(rsa(message, 33, 3))
# print(dechRSA(cipherText,7,33))


import math as m

def rsa(plainText, n, e):
    cipherText = ""
    codeChart = "abcdefghijklmnopqrstuvwxyz"

    for key in plainText:
        if key in codeChart:
            char = codeChart.index(key)
            c = str(int(m.pow(char, e) % n))
            cipherText += c + " "
    
    return cipherText.strip()


def dechRSA(messageChiffre, d, n):
    plainText = ""
    codeChart = "abcdefghijklmnopqrstuvwxyz"
    cipherText = messageChiffre.split()

    for c in cipherText:
        char = int(m.pow(int(c), d) % n)
        if char < len(codeChart):
            plainText += codeChart[char]

    return plainText

# TEST

# plaintext = "hib"
# n = 33
# e = 3
# d = 7

# ciphertext = rsa(plaintext, n, e)
# print(ciphertext)  # Output: "1 13 17"

# decryptedText = dechRSA(ciphertext, d, n)
# print(decryptedText)  # Output: "hib"

