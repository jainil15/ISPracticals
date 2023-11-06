def mono_alphabetic_encryption(plaintext, key):
    ciphertext = ""
    for i in plaintext:
        ciphertext += key[i]
    return ciphertext


def mono_alphabetic_decryption(ciphertext, key):
    inv_key = {v: k for k, v in key.items()}
    plaintext = ""
    for i in ciphertext:
        plaintext += inv_key[i]
    return plaintext


_key = {'a': 'h', 'b': 'm', 'c': 'n', 'd': 't', 'e': 'z', 'f': 'v', 'g': 'b', 'h': 'j', 'i': 's', 'j': 'd', 'k': 'p',
        'l': 'g', 'm': 'x', 'n': 'o', 'o': 'y', 'p': 'q', 'q': 'i', 'r': 'k', 's': 'w', 't': 'u', 'u': 'f', 'v': 'e',
        'w': 'r', 'x': 'a', 'y': 'c', 'z': 'l'}
pt = "jainilpatel"
print("plaintext: ", pt)
print("Key: ", _key)
ct = mono_alphabetic_encryption(pt, _key)
print("ciphertext: ", ct)
print("plaintext: ", mono_alphabetic_decryption(ct, _key))
