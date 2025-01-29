import rsa

(public_key, private_key) = rsa.newkeys(256) # Generate an RSA key pair

with open('public_key.pem', 'wb') as f:
    f.write(public_key.save_pkcs1())

with open('private_key.pem', 'wb') as f:
    f.write(private_key.save_pkcs1())

with open('public_key.pem', 'rb') as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open('private_key.pem', 'rb') as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

message = input("message: ") # Message to encrypt

ciphertext = rsa.encrypt(message.encode(), public_key) # Encrypt the message

plaintext = rsa.decrypt(ciphertext, private_key) # Decrypt the message

print("Original Message: " + message)
print("ciphertext: " + ciphertext.hex())
print("plaintext: " + plaintext.decode()) # Convert the decrypted bytes back to a string
