
def calculate_n(p, q):
    return p * q

def calculate_phi(p, q):
    return (p - 1) * (q - 1)

def calculate_d(e, phi):
    d = 1
    while (d * e) % phi != 1:
        d += 1
    return d

def rsa_encrypt(message, e, n):
    encrypted_message = []
    for char in message:
        encrypted_char = pow(ord(char), e, n)
        encrypted_message.append(encrypted_char)
    return encrypted_message

def main():
    p = 43
    q = 59
    e = 13
    message = "ATTACK"

    n = calculate_n(p, q)
    phi = calculate_phi(p, q)
    d = calculate_d(e, phi)

    encrypted_message = rsa_encrypt(message, e, n)

    print("Encrypted message:", encrypted_message)
    
    
    
# main()
