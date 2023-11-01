def ceaser_encryption(plaintext, shift):
    ciphertext = ""
    for letter in plaintext:
        ciphertext += chr((ord(letter) + shift))
    return ciphertext


def ceaser_decryption(ciphertext, shift):
    plaintext = ""
    for letter in ciphertext:
        plaintext += chr((ord(letter) - shift))
    return plaintext



pt = "Meet me after toga party"
ct = ceaser_encryption(pt, 3)
print(ct)
print(ceaser_decryption(ct, 3))
