import os
import hmac
import hashlib

# Shared secret key (like a password)
secret_key = b"MySecretPassword"

# Step 1: Server generates a nonce (random challenge)
nonce = os.urandom(16)  # 16-byte random number
print("Server sends nonce:", nonce.hex())

# Step 2: Client computes response using HMAC(SHA-256)
client_response = hmac.new(secret_key, nonce, hashlib.sha256).hexdigest()
print("Client sends response:", client_response)

# Step 3: Server verifies response
server_response = hmac.new(secret_key, nonce, hashlib.sha256).hexdigest()

if client_response == server_response:
    print("Authentication successful!")
else:
    print("Authentication failed!")


###############################################################################
Output
Server sends nonce: f10d3828a8e5f7faa23c6547b31e0649
Client sends response: fa6f416e79b4d3a7135cd741b5d32686fbde8087b47f672296b4ebf3720509fa
Authentication successful!