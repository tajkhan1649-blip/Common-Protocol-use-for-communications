from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Step 1: Generate RSA key pair
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Message to be signed
message = b"Hello, this is a secret message!"

# Step 2: Sign the message (using private key)
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Digital Signature:", signature.hex())

# Step 3: Verify the signature (using public key)
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is valid. Message authenticated!")
except:
    print("Signature is invalid. Message has been tampered with!")


###################################################################################

Output
Digital Signature: 2b0450b49bf24e54b73e2c6a9fc6dce62947acd1dad3c0077b7a3e79d9037a92b2415c0fbb
702e0eb2ab228e784d941d4b3beb76ccdeba9e40f0cd76902274b9d37242190d81f5c8de6b9a431020f2613a07bc6200dfe1bde
79c72b9545dca348059f98b297b1263ad5b0b8aa5b79963cf6868767663ce605e8f242c6b20750dfce643cfc848620333e1d619
1b7103b765d2546cdf4f6d61557e0b749606dcef29d95c446afa89fabda8d48d5f609f938f3e7e27d183d16612e9f1ab01eb3e
88952c377a2e678ee9408dc59ee5162007b0bb0def4953c0d4952047270e2297cabbc38ed3b8a668a84ef720297c39c56c6b51
98884b686cf782314b810575a388
Signature is valid. Message authenticated!
