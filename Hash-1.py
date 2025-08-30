import hashlib

# Sample message
message = "Hello World"

# Create SHA-1 hash
sha1_hash = hashlib.sha1(message.encode()).hexdigest()

print("Message:  ", message)
print("SHA-1 Hash:", sha1_hash)

############################################33

Message:   Hello World
SHA-1 Hash: 0a4d55a8d778e5022fab701977c5d840bbc486d0