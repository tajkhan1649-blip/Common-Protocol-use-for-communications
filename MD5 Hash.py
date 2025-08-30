
import hashlib

# Sample message
message = "Hello World"

# Create MD5 hash
md5_hash = hashlib.md5(message.encode()).hexdigest()

print("Message: ", message)
print("MD5 Hash:", md5_hash)

###################################################3

Message:  Hello World
MD5 Hash: b10a8db164e0754105b7a99be72e3fe5

