import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Load public key (from B1)
with open("clinic_public_key.pem", "rb") as f:
    # Load the PEM-encoded public key into a usable object
    public_key = serialization.load_pem_public_key(f.read())

# Load private key (from B1)
with open("clinic_private_key.pem", "rb") as f:
    # Load the PEM-encoded private key (no password protection)
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

# Short message (Patient ID) represented as bytes
patient_id = b"123"
print("Plaintext (Patient ID):", patient_id.decode()) # Display the original plaintext

# RSA Encryption with public key
# Encrypt the patient ID using RSA-OAEP padding with SHA-256
ciphertext = public_key.encrypt(
    patient_id,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)


# Encode the ciphertext into Base64 for readable output
ciphertext_b64 = base64.b64encode(ciphertext).decode()
print("Ciphertext (Base64):", ciphertext_b64) # Display the encrypted ciphertext in Base64 format

# Decrypt with private key
# Decrypt the ciphertext using the RSA private key and same OAEP parameters
recovered = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Recovered Plaintext:", recovered.decode())
