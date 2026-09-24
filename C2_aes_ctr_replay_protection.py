import time, os, base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Session key derived from C1 (Diffie–Hellman) 
session_secret = 2

# Convert the shared secret into a 16-byte value to be used as an AES-128 key
session_key = session_secret.to_bytes(16, byteorder="big")

#Display the derived AES session key in Base64 format
print("Derived Session Key (AES-128, Base64):",
      base64.b64encode(session_key).decode())
print()

# Sender side 
medical_message = "Patient: Ali Ahmad | Diagnosis: Seasonal Flu | Prescription: Paracetamol 500mg twice daily"

current_time = int(time.time())   # Generate a timestamp to ensure message freshness    
unique_nonce = os.urandom(8)     # Generate a unique random nonce to prevent replay attacks     
ctr_iv = os.urandom(16)    # Generate a random nonce/IV for AES-CTR (must be new for each encryption)

  # Combine timestamp, nonce, and medical message into one payload          
data_packet = f"{current_time}|{unique_nonce.hex()}|{medical_message}".encode()

# Create an AES cipher object in CTR mode using the session key and IV
cipher_enc = Cipher(algorithms.AES(session_key), modes.CTR(ctr_iv))
enc_ctx = cipher_enc.encryptor()# Create an encryptor context

# Encrypt the payload
encrypted_data = enc_ctx.update(data_packet) + enc_ctx.finalize()

print("[TRANSMITTER SIDE]")
print("AES-CTR IV (Base64):", base64.b64encode(ctr_iv).decode())
print("Message Identifier (Base64):", base64.b64encode(unique_nonce).decode())
print("Encrypted Payload (Base64):", base64.b64encode(encrypted_data).decode())
print()

# Receiver 
received_nonces = set() # Set to store previously received nonces (used for replay detection)
ALLOWED_TIME_GAP = 60   # Maximum allowed time difference (in seconds) for message freshness

# Function to process an incoming encrypted message
def process_incoming_message(enc_msg, ctr_iv_recv, time_recv, nonce_recv):
    current = int(time.time()) # Get the current system time

    # Replay protection, reject message if nonce was already used
    if nonce_recv in received_nonces:
        print(" Incoming data discarded,, replay attempt detected")
        return

    # # Timestamp validation, reject message if it is outside the allowed time window
    if abs(current - time_recv) > ALLOWED_TIME_GAP:
        print(" Incoming data discarded,, timestamp outside valid window")
        return

    received_nonces.add(nonce_recv)  # Mark nonce as used to prevent future replay

# Create AES-CTR cipher for decryption using the same session key and IV
    cipher_dec = Cipher(algorithms.AES(session_key), modes.CTR(ctr_iv_recv))
    
    dec_ctx = cipher_dec.decryptor() # Create a decryptor context
    original_message = dec_ctx.update(enc_msg) + dec_ctx.finalize() # Decrypt the encrypted payload

    print(" Data accepted ")
    print("Recovered plaintext message:")
    print(original_message.decode())

print("answer 1 → Expected result: VALID MESSAGE")
process_incoming_message(encrypted_data, ctr_iv, current_time, unique_nonce)
print()

print("answer 2 → Expected result: REPLAY REJECTED")
process_incoming_message(encrypted_data, ctr_iv, current_time, unique_nonce)
