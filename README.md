The code is compiled using Google colab

###############################################
SHA-1 Hash

Import the hashlib library to use hashing algorithms.

Define a sample message: "Hello World".

Convert the message into bytes using .encode() because hashing functions require byte input.

Apply the SHA-1 hashing algorithm with hashlib.sha1().

Convert the result into a hexadecimal string using .hexdigest().

Print the original message and its SHA-1 hash

############################################################

SHA-256 hash
 Import the hashlib library, which provides different hashing algorithms.
 
•  Define a sample message: "Hello World".

•  Convert the message into bytes using .encode(), since hashing functions process byte data.

•  Apply the SHA-256 hashing algorithm using hashlib.sha256().

•  Convert the result into a hexadecimal string with .hexdigest().

•  Print both the original message and its SHA-256 hash

################################################################

MD5

•	Import the hashlib library to access hashing algorithms.

•	Define a sample message: "Hello World".

•	Convert the message into bytes using .encode(), since hashing requires byte input.

•	Apply the MD5 hashing algorithm using hashlib.md5().

•	Convert the resulting hash into a hexadecimal string with .hexdigest().

•	Print the original message and its MD5 hash (b10a8db164e0754105b7a99be72e3fe5).

#########################################################

Substitution Cipher 

•	Import the string and random libraries to work with alphabets and random shuffling.

•	Generate a key:

o	Create a list of uppercase alphabets (A–Z).

o	Shuffle the list randomly.

o	Map each original letter to a new letter, forming a substitution key (e.g., 'A': 'M', 'B': 'U', etc.).

•	Encryption function:

o	Convert plaintext to uppercase.

o	Replace each letter with its corresponding letter from the substitution key.

o	Leave non-alphabet characters (e.g., spaces) unchanged.

•	Decryption function:

o	Reverse the substitution key (map cipher letters back to original letters).

o	Replace each encrypted character with its original letter.

o	Preserve non-alphabet characters.

•	Main program flow:

o	Generate a random substitution key.

o	Define a message ("HELLO WORLD").

o	Encrypt the message using the key → produces PONNJ WJVND.

o	Decrypt the ciphertext using the same key → recovers the original "HELLO WORLD".

•	Output shows the substitution key, the original message (plaintext), the encrypted version, and the correctly decrypted message.



##############################3

HMAC-based authentication

•	Import os, hmac, and hashlib libraries to generate randomness and compute secure hashes.

•	Define a shared secret key (MySecretPassword) that is known to both the client and the server.

•	Server step: Generate a random nonce (16-byte random value) using os.urandom(16) and send it to the client as a challenge.

•	Client step: Compute a secure response by applying HMAC with SHA-256 to the nonce using the shared secret key.

•	Server verification: Independently compute the expected HMAC of the nonce using the same secret key.

•	Compare the client’s response with the server’s expected response:

o	If they match → authentication is successful.

o	If they differ → authentication fails.

•	Output example:

o	Server sends nonce: f10d3828a8e5f7faa23c6547b31e0649

o	Client response: fa6f416e79b4d3a7135cd741b5d32686fbde8087b47f672296b4ebf3720509fa

o	Authentication: successful ✅

########################################3

RSA digital signature code 

•	Import cryptographic primitives from the cryptography library (hashes, rsa, and padding).

•	Step 1: Key Generation

o	Generate an RSA key pair with a 2048-bit size and public exponent 65537.

o	Extract the public key from the private key.

•	Step 2: Signing

o	Define a message: "Hello, this is a secret message!".

o	Use the private key to generate a digital signature over the message.

o	Apply PSS (Probabilistic Signature Scheme) padding with MGF1 and SHA-256 as the hashing function.

o	The signature is output as a large hexadecimal string.

•	Step 3: Verification

o	Use the public key to verify the signature against the original message.

o	If the signature matches → print “Signature is valid. Message authenticated!”.

o	If verification fails (message tampered or signature invalid) → print “Signature is invalid. Message has been tampered with!”.

•	Output example:

o	A long digital signature (hexadecimal string).

o	Confirmation: Signature is valid. Message authenticated! ✅



#########################################3


Password + OTP authentication code 

Import the random library to generate a one-time password (OTP).

•	Step 1: Password check

o	Store a predefined password ("MySecretPassword").

o	Prompt the user to enter their password.

o	If the input does not match the stored password → print “Authentication failed!”.

•	Step 2: OTP generation (if password is correct)

o	Generate a random 6-digit OTP using random.randint(100000, 999999).

o	Display the OTP (in real systems, it would be sent via SMS/email, not printed).

o	Prompt the user to enter the OTP.

•	Step 3: OTP validation

o	If the user-entered OTP matches the generated OTP → print “Authentication successful! Access granted.” ✅

o	Otherwise → print “Authentication failed! Invalid OTP.” ❌

•	Output example:

o	User enters correct password.

o	OTP generated: 529792.

o	User enters same OTP → authentication succeeds.


###########################################3

Vigenère Cipher code 

Key Generation

o	The function generate_key() repeats the keyword so that its length matches the message.

o	Example: Message = "HELLO WORLD" (11 characters), Key = "KEY" → repeated key = "KEYKEYKEYKE".

•	Encryption (encrypt() function)

o	Convert the plaintext to uppercase.

o	Match it with the repeated key.

o	For each letter:

	Compute the shift using (ord(p) + ord(k)) % 26.

	Convert the result back into a character (A–Z).

o	Non-alphabetic characters (like spaces) are kept unchanged.

o	Example: "HELLO WORLD" → "RIJVS GSPVH".

•	Decryption (decrypt() function)

o	Generate the repeated key again.

o	For each letter in ciphertext:

	Reverse the shift using (ord(c) - ord(k) + 26) % 26.

	Convert back into the original character.

o	Non-alphabetic characters remain unchanged.

o	Example: "RIJVS GSPVH" → "HELLO WORLD".

•	Main Program

o	Message: "HELLO WORLD".

o	Keyword: "KEY".

o	Encrypted: "RIJVS GSPVH".

o	Decrypted: "HELLO WORLD".
