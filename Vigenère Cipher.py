
# Vigenère Cipher Implementation in Python

# Function to repeat the key so it matches the length of the message
def generate_key(message, key):
    key = list(key.upper())
    if len(message) == len(key):
        return "".join(key)
    else:
        return "".join([key[i % len(key)] for i in range(len(message))])

# Function to encrypt the plaintext
def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = generate_key(plaintext, key)
    ciphertext = ""

    for p, k in zip(plaintext, key):
        if p.isalpha():  # Only encrypt letters
            shift = (ord(p) + ord(k)) % 26
            cipher_char = chr(shift + ord('A'))
            ciphertext += cipher_char
        else:
            ciphertext += p  # Keep spaces/punctuation unchanged
    return ciphertext

# Function to decrypt the ciphertext
def decrypt(ciphertext, key):
    key = generate_key(ciphertext, key)
    plaintext = ""

    for c, k in zip(ciphertext, key):
        if c.isalpha():
            shift = (ord(c) - ord(k) + 26) % 26
            plain_char = chr(shift + ord('A'))
            plaintext += plain_char
        else:
            plaintext += c
    return plaintext

# Example usage
if __name__ == "__main__":
    message = "HELLO WORLD"
    keyword = "KEY"

    encrypted = encrypt(message, keyword)
    decrypted = decrypt(encrypted, keyword)

    print("Message:   ", message)
    print("Keyword:   ", keyword)
    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypted)

###############################################################################

Message:    HELLO WORLD
Keyword:    KEY
Encrypted:  RIJVS GSPVH
Decrypted:  HELLO WORLD
