valeur_hex = input("Entrer des valeurs en Hex : ")

valeur_dec = int(valeur_hex, 16)

print("valeur decimale : ", valeur_dec)


val = input("Entrer une valeur : ")
conv = bytes.fromhex(val.encode().hex())

print("valeur de val en Hex : ", conv)