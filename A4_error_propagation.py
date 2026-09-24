from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from copy import deepcopy

print(" A4: Error Propagation in AES-CBC vs AES-CTR ")
plaintext = "Patient: Ali Ahmad | Diagnosis: Seasonal Flu | Prescription: Paracetamol 500mg twice daily"
plaintext_bytes = plaintext.encode("utf-8")

print("\nPlaintext:")
print(plaintext)

# Key & IV / Nonce
key = get_random_bytes(16)  ## Generate a random 128-bit AES key      
iv = get_random_bytes(16)  #for cbc mode       
nonce = get_random_bytes(8)   #for ctr mode     

print("\nAES Key (HEX):", key.hex().upper())
print("IV (CBC) (HEX):", iv.hex().upper()) #convert iv from byte to hex,upper Converts all lowercase letters in that hexadecimal string to uppercase. 
print("Nonce (CTR) (HEX):", nonce.hex().upper())

# AES-CBC Encryption
cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
cbc_ciphertext = cipher_cbc.encrypt(pad(plaintext_bytes, 16))
# AES-CTR Encryption
cipher_ctr = AES.new(key, AES.MODE_CTR, nonce=nonce)
ctr_ciphertext = cipher_ctr.encrypt(plaintext_bytes)

print("\n--- ORIGINAL CIPHERTEXTS ---")
print("CBC Ciphertext (HEX):", cbc_ciphertext.hex().upper())
print("CTR Ciphertext (HEX):", ctr_ciphertext.hex().upper())

# Modify ONE byte in ciphertext
cbc_modified = bytearray(deepcopy(cbc_ciphertext))
ctr_modified = bytearray(deepcopy(ctr_ciphertext))

cbc_modified[10] ^= 0x01   # flip one bit
ctr_modified[10] ^= 0x01   # flip one bit

print("\n--- MODIFIED CIPHERTEXTS (1 byte changed at index 10) ---")
print("Modified CBC (HEX):", bytes(cbc_modified).hex().upper())
print("Modified CTR (HEX):", bytes(ctr_modified).hex().upper())

# CBC Decryption
cipher_cbc_dec = AES.new(key, AES.MODE_CBC, iv)
cbc_decrypted = cipher_cbc_dec.decrypt(bytes(cbc_modified))

# CTR Decryption
cipher_ctr_dec = AES.new(key, AES.MODE_CTR, nonce=nonce)
ctr_decrypted = cipher_ctr_dec.decrypt(bytes(ctr_modified))

print("\n--- DECRYPTED RESULTS AFTER MODIFICATION ---")
print("CBC Decrypted (raw):", cbc_decrypted)
print("CTR Decrypted:", ctr_decrypted.decode(errors="replace"))
