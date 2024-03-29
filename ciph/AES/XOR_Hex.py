def xor_hex(a, b):
    # Convertir les valeurs hexadécimales en entiers
    a_decimal = int(a, 16)
    b_decimal = int(b, 16)

    # Effectuer le XOR entre les entiers
    resultat_decimal = a_decimal ^ b_decimal

    # Convertir le résultat en représentation hexadécimale
    resultat_hex = hex(resultat_decimal)[2:]  # [2:] pour retirer le préfixe '0x'

    return resultat_hex


# Exemple d'utilisation
valeur_hex1 = input("Entrez la première valeur hexadécimale : ")
valeur_hex2 = input("Entrez la deuxième valeur hexadécimale : ")

resultat = xor_hex(valeur_hex1, valeur_hex2)
print("Résultat du XOR en hexadécimal :", resultat)
