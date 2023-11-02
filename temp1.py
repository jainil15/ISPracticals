h0 = 0x67452301
h1 = 0xEFCDAB89
h2 = 0x98BADCFE
h3 = 0x10325476
h4 = 0xC3D2E1F0



def leftRotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF


def add_padding(binary_string):

    padding_length = 512 - len(binary_string)

    binary_string += '1' + '0' * (padding_length - 64 - 1) + convert_to_binary(len(binary_string), 64)
    print(binary_string)
    return binary_string


def hash_function(bin_string):
    global h0, h1, h2, h3, h4
    bin_string = add_padding(bin_string)
    w = [int(bin_string[i:i + 32], 2) for i in range(0, 512, 32)]
    print(len(w))
    print(w)
    for i in range(16, 80):
        w.append(leftRotate(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1))

    a, b, c, d, e = h0, h1, h2, h3, h4

    for i in range(80):
        if 0 <= i <= 19:
            f = (b & c) | ((~b) & d)
            k = 0x5A827999
        elif 20 <= i <= 39:
            f = b ^ c ^ d
            k = 0x6ED9EBA1
        elif 40 <= i <= 59:
            f = (b & c) | (b & d) | (c & d)
            k = 0x8F1BBCDC
        elif 60 <= i <= 79:
            f = b ^ c ^ d
            k = 0xCA62C1D6

        temp = (leftRotate(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
        e = d
        d = c
        c = leftRotate(b, 30)
        b = a
        a = temp

    h0 = (h0 + a) & 0xFFFFFFFF
    h1 = (h1 + b) & 0xFFFFFFFF
    h2 = (h2 + c) & 0xFFFFFFFF
    h3 = (h3 + d) & 0xFFFFFFFF
    h4 = (h4 + e) & 0xFFFFFFFF

    return hex(h0)[2:] + hex(h1)[2:] + hex(h2)[2:] + hex(h3)[2:] + hex(h4)[2:]



def convert_to_binary(number, block_size):
    return '0' * (block_size - len(bin(number)[2:]) % block_size) + bin(number)[2:]


def convert_bin_to_hex(binary_string):
    return hex(int(binary_string))


def main():
    bin_ = "011000010110001001100011"
    hash_ = hash_function(bin_)
    print("Hash: ", hash_)


if __name__ == '__main__':
    main()
