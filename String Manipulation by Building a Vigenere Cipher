# Vigenere Cipher Encryption

# Decrypted Example
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

# Encrypted Example
# text = 'Hello World!'
# custom_key = 'python'

def vigenere(message, key, direction = 1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalnum():
            encrypted_text += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            encrypted_text += alphabet[new_index]

    return encrypted_text

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'Text: {text}')
print(f'Key: {custom_key}')

encryption = encrypt(text, custom_key)
print(f'\nEncrypted text: {encryption}')
decryption = decrypt(text, custom_key)
print(f'Decrypted text: {decryption}')
