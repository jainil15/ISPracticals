import math
import random
from sympy import primitive_root

h0 = 0x67452301
h1 = 0xEFCDAB89
h2 = 0x98BADCFE
h3 = 0x10325476
h4 = 0xC3D2E1F0


def public_key_gen(private_key, q, alpha):
    public_key = pow(alpha, private_key) % q
    return public_key


def calc_key(public_key, private_key, q):
    k = pow(public_key, private_key) % q
    return k

def compute_k(q):
    q = q - 1
    for i in reversed(range(3, q // 2)):
        if math.gcd(q, i) == 1:
            return 5


def compute_modulo(a, b):
    k = 0
    while True:
        if a * k % b == 1:
            return k
        k += 1



def main():
    prime_num = 19
    alpha_ = 10
    Xa = 16
    Ya = public_key_gen(private_key=Xa, q=prime_num, alpha=alpha_)

    print("Xa =", Xa, "\nYa =", Ya)
    # key = calc_key(private_key=Xa, public_key=Yb, q=prime_num)
    # print("Key for A =", key)
    # key = calc_key(private_key=Xb, public_key=Ya, q=prime_num)
    # print("Key for B =", key)
    # ----
    hash_value = 14
    k = compute_k(prime_num)
    print("K: ", k)
    s1 = calc_key(alpha_, k, prime_num)
    print("Modulo inverse: ", compute_modulo(k, prime_num - 1))
    s2 = compute_modulo(k, prime_num-1)*(hash_value - (Xa*s1)) % (prime_num-1)
    v1 = pow(alpha_, hash_value) % prime_num
    v2 = (pow(Ya, s1)*pow(s1, s2)) % prime_num
    print("V1: ", v1, "\nV2: ", v2)


if __name__ == '__main__':
    main()
