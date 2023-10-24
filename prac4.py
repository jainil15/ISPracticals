def vigenere_encryption(plaintext, key):
    ciphertext = ''
    for i in range(len(plaintext)):
        ciphertext += chr((((ord(plaintext[i]) - 97) + (ord(key[i % len(key)]) - 97)) % 26) + 97)
    return ciphertext


def vigenere_decryption(ciphertext, key):
    plaintext = ''
    for i in range(len(ciphertext)):
        plaintext += chr((((ord(ciphertext[i]) - 97) - (ord(key[i % len(key)]) - 97)) % 26) + 97)
    return plaintext


pt = "jainilpatel"
key = "vigenere"
ct = vigenere_encryption(pt, key)
print(ct)
print(vigenere_decryption(ct, key))
