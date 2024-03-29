def galois_multiplication(a, b):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11B
        b >>= 1
    return p

# # Exemple d'utilisation
# # a = 0xDB
# # b = 0x13
# while(True):
#     a = input("Entrer la valeur de a : ")
#     b = input("Entrer la valeur de b : ")
#     # a = int(a)
#     # b = int(b)
#     aa = ("0x"+a)
#     bb = int("0x"+b)
#     print("Converted : ", aa)
#     print("Converted : ", bb)
#     # aa = int(aa)
#     # bb = int(bb)
    
    # resultat = galois_multiplication(a, b)
    # print("Résultat de la multiplication hexadécimale :", hex(resultat))
a = 0x03
b = 0xc7

resultat = galois_multiplication(a, b)
print("Résultat de la multiplication hexadécimale :", hex(resultat))
