def public_key_gen(private_key, q, alpha):
    public_key = pow(alpha, private_key) % q
    return public_key


def calc_key(public_key, private_key, q):
    k = pow(public_key, private_key) % q
    return k


prime_num = 283
alpha_ = 119
Xa = 124
Xb = 202
Ya = public_key_gen(private_key=Xa, q=prime_num, alpha=alpha_)
Yb = public_key_gen(private_key=Xb, q=prime_num, alpha=alpha_)
print("Xa =", Xa, "\nXb =", Xb, "\nYa =", Ya, "\nYb =", Yb)
key = calc_key(private_key=Xa, public_key=Yb, q=prime_num)
print("Key for A =", key)
key = calc_key(private_key=Xb, public_key=Ya, q=prime_num)
print("Key for B =", key)