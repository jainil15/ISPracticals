KEYS = [[0] * 4 for i in range(44)]
s_box = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
]

rcon_values = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]


def gmul(a, b):
    if b == 1:
        return a
    tmp = (a << 1) & 0xff
    if b == 2:
        return tmp if a < 128 else tmp ^ 0x1b
    if b == 3:
        return gmul(a, 2) ^ a


def create_matrix(plaintext):
    matrix = [[0 for i in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            matrix[i][j] = hex(int(plaintext[j * 8 + 2 * i: j * 8 + 2 * i + 2], 16))

    return matrix


def key_generation(word):
    round_ = 0
    rot_word = []
    matrix = [[0] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            matrix[j][i] = hex(int(word[j * 8 + 2 * i: j * 8 + 2 * i + 2], 16))
    while round_ <= 10:

        if round_ > 0:
            sub_word = [hex(s_box[int(i, 16)]) for i in rot_word]
            rcon = rcon_values[round_ - 1]
            z = [hex(int(sub_word[0], 16) ^ rcon), sub_word[1], sub_word[2], sub_word[3]]

            KEYS[round_ * 4 + 0] = [hex(int(KEYS[(round_ - 1) * 4][i], 16) ^ int(z[i], 16)) for i in range(4)]
            KEYS[round_ * 4 + 1] = [hex(int(KEYS[(round_ - 1) * 4 + 1][i], 16) ^ int(KEYS[round_ * 4 + 0][i], 16)) for i
                                    in range(4)]
            KEYS[round_ * 4 + 2] = [hex(int(KEYS[(round_ - 1) * 4 + 2][i], 16) ^ int(KEYS[round_ * 4 + 1][i], 16)) for i
                                    in range(4)]
            KEYS[round_ * 4 + 3] = [hex(int(KEYS[(round_ - 1) * 4 + 3][i], 16) ^ int(KEYS[round_ * 4 + 2][i], 16)) for i
                                    in range(4)]

            round_ += 1

        else:
            KEYS[round_ * 4 + 0] = matrix[0]
            KEYS[round_ * 4 + 1] = matrix[1]
            KEYS[round_ * 4 + 2] = matrix[2]
            KEYS[round_ * 4 + 3] = matrix[3]
            round_ += 1
        rot_word = []
        for i in range(4):
            rot_word.append(KEYS[((round_ - 1) * 4 + 3)][(i + 1) % 4])


def sub_bytes(matrix):
    for i in range(4):
        for j in range(4):
            matrix[i][j] = hex(s_box[int(matrix[i][j], 16)])
    return matrix


def shift_rows(matrix):
    new_matrix = [[0] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            new_matrix[i][j] = matrix[i][(j + i) % 4]

    return new_matrix


def mix_columns(matrix):
    for i in range(4):
        a = int(matrix[0][i], 16)
        b = int(matrix[1][i], 16)
        c = int(matrix[2][i], 16)
        d = int(matrix[3][i], 16)
        matrix[0][i] = hex(gmul(a, 2) ^ gmul(b, 3) ^ c ^ d)
        matrix[1][i] = hex(a ^ gmul(b, 2) ^ gmul(c, 3) ^ d)
        matrix[2][i] = hex(a ^ b ^ gmul(c, 2) ^ gmul(d, 3))
        matrix[3][i] = hex(gmul(a, 3) ^ b ^ c ^ gmul(d, 2))

    return matrix


def add_round_key(matrix, round_key):
    for i in range(4):
        for j in range(4):
            matrix[i][j] = hex(int(matrix[i][j], 16) ^ int(round_key[i][j], 16))
    return matrix


def aes_encryption(plaintext, keys):
    round_ = 0
    ct = create_matrix(plaintext)
    while round_ <= 10:

        round_key = KEYS[round_ * 4:round_ * 4 + 4]
        round_key = [[row[i] for row in round_key] for i in range(len(round_key[0]))]
        if round_ == 0:
            ct = add_round_key(ct, round_key)
        elif round_ == 10:
            ct = sub_bytes(ct)
            ct = shift_rows(ct)
            ct = add_round_key(ct, round_key)
        else:
            ct = sub_bytes(ct)
            ct = shift_rows(ct)
            ct = mix_columns(ct)
            ct = add_round_key(ct, round_key)

        round_ += 1
    return ct


plaintext = "0123456789abcdeffedcba9876543210"
key = "0f1571c947d9e8590cb7add6af7f6798"
key_generation(key)
ciphertext = aes_encryption(plaintext, KEYS)
print(ciphertext)