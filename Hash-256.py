import hashlib

# Sample message
message = "Hello World"

# Create SHA-256 hash
sha256_hash = hashlib.sha256(message.encode()).hexdigest()

print("Message:    ", message)
print("SHA-256 Hash:", sha256_hash)


#################################################

Message:     Hello World
SHA-256 Hash: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
