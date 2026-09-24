# A3 - AES Encryption (CBC Mode)

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

print(" AES Encryption using CBC Mode ")
plaintext = "Patient: Ali Ahmad | Diagnosis: Seasonal Flu | Prescription: Paracetamol 500mg twice daily"
print("\nPlaintext Message:")
print(plaintext)

plaintext_bytes = plaintext.encode("utf-8")
#  AES Key (128-bit)
key = get_random_bytes(16)   
print("\nAES Key (HEX):")
print(key.hex().upper())

#  IV (16 bytes)
iv = get_random_bytes(16)
print("\nIV (HEX):")
print(iv.hex().upper())

#  Encryption (CBC)
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext_bytes, 16))

#  Decryption
cipher_dec = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(cipher_dec.decrypt(ciphertext), 16)

print("\n--- RESULTS ---")
print("Ciphertext (HEX):", ciphertext.hex().upper())
print("Decrypted Plaintext:", decrypted.decode("utf-8"))
