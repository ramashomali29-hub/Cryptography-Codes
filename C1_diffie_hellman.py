

# Fast modular exponentiation function
# Computes (base^exp) mod mod efficiently
def mod_exp(base, exp, mod):
    result = 1
    base %= mod # Reduce base modulo mod
    while exp > 0: # Repeat until exponent becomes zero
        if exp % 2 == 1: # If exponent is odd
            result = (result * base) % mod # Multiply result by base
        base = (base * base) % mod # Square the base
        exp //= 2 # Divide exponent by 2
    return result

# Public parameters
p = 23 # Large prime number (public)
g = 5  # Generator (public)

print("Public parameters:")
print("p =", p)
print("g =", g)

# Private keys
a = 6   # Doctor private key
b = 15  # Patient private key

# Public values exchanged
A = mod_exp(g, a, p) # Compute Doctor's public value A = g^a mod p
B = mod_exp(g, b, p) # Compute Patient's public value B = g^b mod p

print("\nDoctor public value A:", A)
print("Patient public value B:", B)

# Shared secret
doctor_shared_key = mod_exp(B, a, p) # Doctor computes shared secret using patient's public value
patient_shared_key = mod_exp(A, b, p) # Patient computes shared secret using doctor's public value

print("\nDoctor derived session key:", doctor_shared_key)
print("Patient derived session key:", patient_shared_key)

print("\nKeys match:", doctor_shared_key == patient_shared_key) 
# Check that both sides derived the same session key
