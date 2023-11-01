def to_int(x):
    return ord(x) - 97


def to_chr(x):
    return chr(x % 26 + 97)


def calc_mod(x):
    i = 1
    while True:
        if (i * x) % 26 == 1:
            return i
        else:
            i += 1


def inverse_matrix(matrix):
    inv_det = calc_mod(to_int(matrix[0][0]) * to_int(matrix[1][1]) - to_int(matrix[0][1]) * to_int(matrix[1][0]))
    inv_matrix = [[(to_int(matrix[1][1]) * inv_det) % 26, (-to_int(matrix[0][1]) * inv_det) % 26],
                  [(-to_int(matrix[1][0]) * inv_det) % 26, (to_int(matrix[0][0]) * inv_det) % 26]]
    return inv_matrix


def create_tupples(plaintext):
    tupples = []
    i = 0
    while i < len(plaintext):
        if (i + 1) < len(plaintext):
            tupples.append((plaintext[i], plaintext[i + 1]))
            i += 2
        else:
            tupples.append((plaintext[i], 'x'))
            i += 1

    return tupples


def hill_cipher_encryption(plaintext, key):
    ciphertext = ''
    key_matrix = [[0] * 2 for i in range(2)]
    for i in range(2):
        for j in range(2):
            key_matrix[i][j] = key[i * 2 + j]

    plaintext_tuples = create_tupples(plaintext)

    for i in plaintext_tuples:
        x1 = to_chr(to_int(i[0]) * to_int(key_matrix[0][0]) + to_int(i[1]) * to_int(key_matrix[0][1]))
        x2 = to_chr(to_int(i[0]) * to_int(key_matrix[1][0]) + to_int(i[1]) * to_int(key_matrix[1][1]))
        ciphertext += x1 + x2

    return ciphertext


def hill_cipher_decryption(ciphertext, key):
    plaintext = ''
    key_matrix = [[0] * 2 for i in range(2)]

    for i in range(2):
        for j in range(2):
            key_matrix[i][j] = key[i * 2 + j]
    inv_matrix = inverse_matrix(key_matrix)
    ciphertext_tuples = create_tupples(ciphertext)

    for i in ciphertext_tuples:
        x1 = to_chr(to_int(i[0]) * inv_matrix[0][0] + to_int(i[1]) * inv_matrix[0][1])
        x2 = to_chr(to_int(i[0]) * inv_matrix[1][0] + to_int(i[1]) * inv_matrix[1][1])
        plaintext += x1 + x2

    return plaintext


pt = "jainilpatel"
key = "hill"
print("plaintext: ", pt, "key: ", key)
ct = hill_cipher_encryption(pt, key)
print("ciphertext: ", ct)
print("plaintext: ", hill_cipher_decryption(ct, key))

