# A1SHA-256 Hashing

import hashlib

print(" SHA-256 Hashing:")

plaintext = "Patient: Ali Ahmad | Diagnosis: Seasonal Flu | Prescription: Paracetamol 500mg twice daily"

print("\nPlaintext Message:")
print(plaintext)

# Convert plaintext to bytes
plaintext_bytes = plaintext.encode('utf-8')

# apply SHA-256
hash_object = hashlib.sha256(plaintext_bytes)
hash_hex = hash_object.hexdigest()

# output hash in HEX
print("\nSHA-256 Hash (HEX):")
print(hash_hex)
