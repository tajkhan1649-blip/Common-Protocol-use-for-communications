import string
import random

# Generate a random substitution key (permutation of the alphabet)
def generate_key():
    alphabet = list(string.ascii_uppercase)
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))

# Encrypt with substitution cipher
def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    ciphertext = ""
    for char in plaintext:
        if char in key:
            ciphertext += key[char]
        else:
            ciphertext += char
    return ciphertext

# Decrypt with substitution cipher
def decrypt(ciphertext, key):
    reverse_key = {v: k for k, v in key.items()}
    plaintext = ""
    for char in ciphertext:
        if char in reverse_key:
            plaintext += reverse_key[char]
        else:
            plaintext += char
    return plaintext

# Example usage
if __name__ == "__main__":
    key = generate_key()
    print("Substitution Key:", key)

    message = "HELLO WORLD"
    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)

    print("Plaintext: ", message)
    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypted)


#############################
output 
Substitution Key: {'A': 'M', 'B': 'U', 'C': 'I', 'D': 'D', 'E': 'O', 'F': 'X', 'G': 'G', 'H': 'P', 'I': 'T', 'J': 'S', 'K': 'B', 'L': 'N', 'M': 'H', 'N': 'Z', 'O': 'J', 'P': 'Q', 'Q': 'K', 'R': 'V', 'S': 'R', 'T': 'A', 'U': 'E', 'V': 'L', 'W': 'W', 'X': 'F', 'Y': 'Y', 'Z': 'C'}
Plaintext:  HELLO WORLD
Encrypted:  PONNJ WJVND
Decrypted:  HELLO WORLD
