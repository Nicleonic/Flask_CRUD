def mixcolumn(octet):
    # Matrice fixe utilisée pour l'opération MixColumns
    matrix = [[0x02, 0x03, 0x01, 0x01],
              [0x01, 0x02, 0x03, 0x01],
              [0x01, 0x01, 0x02, 0x03],
              [0x03, 0x01, 0x01, 0x02]]

    result = [0] * 4  # Liste pour stocker les octets résultants

    for i in range(4):
        for j in range(4):
            # Multiplication dans le domaine de Galois
            if matrix[i][j] == 0x01:
                result[i] ^= octet[j]
            elif matrix[i][j] == 0x02:
                result[i] ^= (octet[j] << 1) ^ (0x1B if (octet[j] & 0x80) else 0)
            elif matrix[i][j] == 0x03:
                result[i] ^= (octet[j] << 1) ^ octet[j] ^ (0x1B if (octet[j] & 0x80) else 0)

    return result


# Exemple d'utilisation
# octet = [0xDB, 0x13, 0x53, 0x45]
# octet = [0x63, 0x2f, 0xaf, 0xa2]
# octet = [0xeb, 0x93, 0xc7, 0x20]
# octet = [0x9f, 0x92, 0xab, 0xcb]
# octet = [0xa0, 0xc0, 0x30, 0x2b]
# octet = [0x1a, 0xc7, 0xe9, 0x9a]
octet = [0x27, 0xb4, 0x24, 0xbb]



resultat = mixcolumn(octet)
print("Résultat de MixColumns :", [hex(octet) for octet in resultat])