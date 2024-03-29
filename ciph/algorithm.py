
def calculate_n(p, q):
    return p * q

def calculate_phi(p, q):
    return (p - 1) * (q - 1)

def calculate_d(e, phi):
    d = 1
    while (d * e) % phi != 1:
        d += 1
    return d


def euclid_etendu(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        pgcd, x, y = euclid_etendu(b % a, a)
        return (pgcd, y - (b // a) * x, x)

def calculer_cle_privee(e, n):
    pgcd, x, y = euclid_etendu(e, n)
    if pgcd != 1:
        return "La clé privée ne peut pas être calculée car e et n ne sont pas premiers entre eux."
    else:
        d = x % n
        return d

# Exemple d'utilisation
e = 65537
n = 1437177

# e =17
# n =323
# d =275

# e =11
# n =391
# d =59

# e = 23
# n = 391
# d = 187
# e = 23
# n = 247, 246, 245 --> d : 43, 107, 32
cle_privee = calculer_cle_privee(23 , 245)
print("La clé privée d est :", cle_privee)


# print("Calcul de d \n")
# d = calculate_d(23,216)
# print("d --> : ", d)