import hashlib
import os
import base64

def hash_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

def hash_pbkdf2(password, salt=None, iterations=100_000):
    if salt is None:
        salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, iterations)
    return base64.b64encode(salt).decode(), base64.b64encode(hashed).decode()

def hash_sha512(data):
    return hashlib.sha512(data.encode()).hexdigest()

def hybrid_hash(password):
    print("\n🔐 Hybrid Hashing in Progress...\n")

    # Step 1: SHA-256
    sha256_result = hash_sha256(password)
    print("[1] SHA-256:", sha256_result)

    # Step 2: PBKDF2 (SHA-256 result as input)
    salt, pbkdf2_result = hash_pbkdf2(sha256_result)
    print("[2] PBKDF2-HMAC (w/ salt):", pbkdf2_result)
    print("     Salt (base64):", salt)

    # Step 3: SHA-512 of PBKDF2
    sha512_result = hash_sha512(pbkdf2_result)
    print("[3] Final SHA-512:", sha512_result)

# --- Run example ---
password_input = input("Enter a password to hash: ")
hybrid_hash(password_input)
