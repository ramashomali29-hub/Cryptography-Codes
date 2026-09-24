import math
import hashlib


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    # Check divisibility by odd numbers up to sqrt(num)
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

# Fast modular exponentiation function (Square-and-Multiply)
# Computes (base^expo) mod m efficiently
def power(base, expo, m):
    res = 1
    base = base % m

     # If exponent is odd, multiply result by base
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m # Square the base
        expo >>= 1 # Divide exponent by 2
    return res

#Euclidean Algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1
# Compute modular inverse of e modulo phi
def mod_inverse_extended(e, phi):
    g, x, _ = extended_gcd(e, phi)
    # If gcd(e, phi) != 1, inverse does not exist
    if g != 1:
        return -1
    return x % phi  # Return positive modular inverse

# RSA Key Generation 

def generate_keys_user_input():
    # Read prime numbers p and q from the user
    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))

    n = p * q # Compute modulus n
    phi = (p - 1) * (q - 1)  # Compute Euler's totient function 

    e = 65537  # Choose public exponent e (common secure value)

     # Ensure gcd(e, phi) = 1
    if gcd(e, phi) != 1:
        for i in range(3, phi, 2):
            if gcd(i, phi) == 1:
                e = i
                break

    d = mod_inverse_extended(e, phi)  # Compute private exponent d

    return e, d, n

#  Digital Signature 

print("\n===== B2: RSA Digital Signature (Manual) =====")

# 1. Same plaintext from Part A
plaintext = "Patient: Ali Ahmad | Diagnosis: Seasonal Flu | Prescription: Paracetamol 500mg twice daily"
print("\nPlaintext Message:")
print(plaintext)

# 2. Compute SHA-256 hash
hash_hex = hashlib.sha256(plaintext.encode()).hexdigest()
hash_int = int(hash_hex, 16) # Convert hash from hex to integer

print("\nSHA-256 Hash (HEX):")
print(hash_hex)

# Generate RSA keys
e, d, n = generate_keys_user_input()

print(f"\nPublic key (e, n): ({e}, {n})")
print(f"Private key (d, n): ({d}, {n})")

#  Reduce hash modulo n
hash_int = hash_int % n

# 3. Create digital signature by signing the hash with private key
signature = power(hash_int, d, n)

print("\nDigital Signature (integer):")
print(signature)

# 4. Verify signature (original message)
verified_hash = power(signature, e, n) # Decrypt signature using public key

print("\nVerification Result (Original Message):")
if verified_hash == hash_int:
    print(" Signature verification SUCCESSFUL")
else:
    print(" Signature verification FAILED")

# 5. Alter one character
altered_message = "Patient: Ali Ahmad | Diagnosis: Seasonal Cold | Prescription: Paracetamol 500mg twice daily"
print("\nAltered Message:")
print(altered_message)

# Compute hash of altered message
altered_hash = int(hashlib.sha256(altered_message.encode()).hexdigest(), 16) % n
# Verify signature again using the altered message hash
verified_hash_altered = power(signature, e, n)

print("\nVerification Result (Altered Message):")
if verified_hash_altered == altered_hash:
    print(" Signature verification SUCCESSFUL")
else:
    print(" Signature verification FAILED (message was altered)")
