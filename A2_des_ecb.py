
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

print("DES Encryption using ECB Mode:")


plaintext = "Patient: Ali Ahmad | Diagnosis: Seasonal Flu | Prescription: Paracetamol 500mg twice daily"
print("\nPlaintext Message:")
print(plaintext)

# convert plaintext to bytes
plaintext_bytes = plaintext.encode("utf-8")

#  DES Key64-bit
key_hex = "133457799BBCDFF1"
key = bytes.fromhex(key_hex)
print("\nDES Key (HEX):")
print(key_hex)

# Padding (DES block size = 8 bytes)
plaintext_padded = pad(plaintext_bytes, 8)

#  Encryption 
cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext_padded)

#  Decryption
cipher_dec = DES.new(key, DES.MODE_ECB)
decrypted_padded = cipher_dec.decrypt(ciphertext)
decrypted = unpad(decrypted_padded, 8)

print("\n RESULTS:")
print("Plaintext (HEX):", plaintext_bytes.hex().upper())
print("Ciphertext (HEX):", ciphertext.hex().upper())
print("Decrypted Plaintext:", decrypted.decode("utf-8"))
