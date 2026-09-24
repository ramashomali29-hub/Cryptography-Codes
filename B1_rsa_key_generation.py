from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

#  2048-bit key pair
private_key = rsa.generate_private_key(
    public_exponent=65537, #standard secure value in rsa
    key_size=2048
)

public_key = private_key.public_key()

# Export private key (PEM format)
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# Export public key (PEM format)
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save keys to files
with open("clinic_private_key.pem", "wb") as f:
    f.write(private_pem)

with open("clinic_public_key.pem", "wb") as f:
    f.write(public_pem)

print(" RSA 2048-bit keys generated successfully!")
print(" Private Key: clinic_private_key.pem")
print(" Public Key: clinic_public_key.pem")
