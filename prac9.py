import hashlib


def sha1_hash(plaintext):
    sha1 = hashlib.sha1()
    sha1.update(plaintext.encode('utf-8'))
    hashed = sha1.hexdigest()
    return hashed


plaintext = "Jainil Patel"
sha1_result = sha1_hash(plaintext)
print("SHA-1 Hash:", sha1_result)
