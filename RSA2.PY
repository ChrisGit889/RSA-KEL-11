import rsa

# Generate public and private keys
public_key, private_key = rsa.newkeys(512)

# Ask user for a string
message = input("Enter a string to encrypt: ")

# Encrypt the message using the public key
encrypted_message = rsa.encrypt(message.encode(), public_key)

# Decrypt the message using the private key
decrypted_message = rsa.decrypt(encrypted_message, private_key)

# Print the results
print("\nHasil RSA Encryption:")
print("Teks Asli        :", message)
print("Teks Terenkripsi :", encrypted_message)
print("Teks Didekripsi  :", decrypted_message.decode())
