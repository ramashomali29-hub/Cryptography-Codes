# Secure Medical Messaging – Cryptography Project

A Python implementation of the core cryptographic functions for a secure messaging system that allows doctors to send encrypted medical messages to patients. The system ensures confidentiality, integrity, authentication, secure key exchange, and replay prevention.

## Security Goals
- **Confidentiality:** Messages are encrypted so only the intended patient can read them
- **Integrity:** Any modification to a message is detected
- **Authentication:** Patients can verify that messages come from an authorized doctor
- **Secure Key Exchange:** Session keys are never sent in plaintext
- **Replay Prevention:** Old or repeated messages are rejected

## Implementation

| File | Description |
|---|---|
| `A1_sha256_hash.py` | SHA-256 hashing for integrity protection |
| `A2_des_ecb.py` | DES encryption and decryption in ECB mode |
| `A3_aes_cbc.py` | AES-128 encryption and decryption in CBC mode |
| `A4_error_propagation.py` | Comparison of error propagation in AES-CBC vs AES-CTR |
| `B1_rsa_key_generation.py` | 2048-bit RSA key pair generation in PEM format |
| `B2_rsa_digital_signature.py` | RSA digital signature implemented from scratch, including Square-and-Multiply and the Extended Euclidean Algorithm, with tamper detection |
| `B3_rsa_short_encryption.py` | RSA-OAEP encryption of short messages using the keys from B1 |
| `C1_diffie_hellman.py` | Diffie–Hellman key exchange to derive a shared session key |
| `C2_aes_ctr_replay_protection.py` | AES-CTR session encryption with nonce and timestamp freshness checks |

## Secure Workflow
1. Doctor and patient derive a shared AES session key using Diffie–Hellman
2. The message and metadata (sender ID, nonce, timestamp) are hashed with SHA-256
3. The hash is signed with the clinic's RSA private key
4. The payload is encrypted with AES-CTR using a fresh nonce
5. The receiver checks freshness, decrypts the message, and verifies the signature
6. Tampered or replayed messages are rejected

## Tech Stack
- Python
- PyCryptodome (DES, AES)
- cryptography (RSA, AES-CTR)
- hashlib (SHA-256)

## How to Run
```
pip install pycryptodome cryptography
python A1_sha256_hash.py
```
Run `B1_rsa_key_generation.py` before `B3_rsa_short_encryption.py`, since B3 uses the generated keys.

## Note
Some implementations (B2 and C1) use small parameters and textbook RSA for educational demonstration of the underlying mathematics. Production systems should use large primes, standard padding schemes (such as RSA-PSS), and vetted cryptographic libraries.
