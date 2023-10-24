def calc_d(e, p, q):
    i = 1
    phi_n = (p - 1) * (q - 1)
    d = 0
    while True:
        if e * i % phi_n == 1:
            d = i
            break
        else:
            i += 1
    return d


def rsa_encryption(plaintext: int, e, n):
    return pow(plaintext, e) % n


def rsa_decryption(ciphertext: int, d, n):
    return pow(ciphertext, d) % n


def main():
    p = 17
    q = 19
    e = 29
    d = calc_d(e, p, q)
    n = p * q
    plaintext = 88
    ciphertext = rsa_encryption(plaintext, e=e, n=n)
    print(ciphertext)
    print(rsa_decryption(ciphertext, d=d, n=n))


if __name__ == "__main__":
    main()
