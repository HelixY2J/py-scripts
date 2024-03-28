import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime_number():
    p = random.randint(100, 1000)
    while not is_prime(p):
        p = random.randint(100, 1000)
    return p


def primitive_root(p):
    while True:
        g = random.randint(2, p - 1)
        if pow(g, (p - 1) // 2, p) != 1 and pow(g, p - 1, p) == 1:
            return g


def one_time_pad_key(msg_len):
    key = ""
    for i in range(msg_len):
        key += chr(random.randint(0, 255))
    return key


def encrypt(msg, key):
    encrypted_msg = ""
    for i in range(len(msg)):
        encrypted_msg += chr(ord(msg[i]) ^ ord(key[i]))
    return encrypted_msg


def decrypt(encrypted_msg, key):
    decrypted_msg = ""
    for i in range(len(encrypted_msg)):
        decrypted_msg += chr(ord(encrypted_msg[i]) ^ ord(key[i]))
    return decrypted_msg


def elgamal_key_gen(p, g):
    private_key = random.randint(2, p - 1)
    public_key = pow(g, private_key, p)
    return private_key, public_key


def verify_communication(msg, decrypted_msg):
    if msg == decrypted_msg:
        return True
    else:
        return False


# Generate prime number and primitive root
p = generate_prime_number()
g = primitive_root(p)


group_number = p
print("Group number (p):", group_number)
print("Primitive root (g):", g)


alice_private_key, alice_public_key = elgamal_key_gen(p, g)
bob_private_key, bob_public_key = elgamal_key_gen(p, g)


print("\n> Key Generation Phase ")
print(f"Alice's private key: {alice_private_key}, Alice's public key: {alice_public_key}")
print(f"Bob's private key: {bob_private_key}, Bob's public key: {bob_public_key}")


rounds = 3
for _ in range(rounds):
    
    user_msg = "The cargo leaves today at 2 AM sharp"  

    
    key = one_time_pad_key(len(user_msg))
    encrypted_msg = encrypt(user_msg, key)
    print("\n> Encryption Phase ")
    print("Original message:", user_msg)
    print("One-Time Pad Key:", [ord(c) for c in key])
    print("Encrypted message:", encrypted_msg)

    
    decrypted_msg = decrypt(encrypted_msg, key)
    print("\n> Decryption Phase ")
    print("Decrypted message:", decrypted_msg)
