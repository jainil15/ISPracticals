def create_matrix(key):
    key = key.replace('j', 'i')
    matrix = [[0 for i in range(5)] for j in range(5)]
    row, col = 0, 0
    for letter in key:
        if (row < 5) and (col < 5):
            matrix[row][col] = letter
            col += 1
        if col >= 5:
            row += 1
            col = 0
    for i in range(26):
        if (chr(i + 97) not in key) and chr(i + 97) != 'j':
            if (row < 5) and (col < 5):
                matrix[row][col] = chr(i + 97)
                col += 1
            if col >= 5:
                row += 1
                col = 0
    return matrix


def create_tupples(plaintext):
    tupples = []
    i = 0
    while i < len(plaintext):
        if (i + 1) < len(plaintext):
            if plaintext[i] != plaintext[i + 1]:
                tupples.append((plaintext[i], plaintext[i + 1]))
                i += 2
            else:
                tupples.append((plaintext[i], 'x'))
                i += 1
        else:
            tupples.append((plaintext[i], 'x'))
            i += 1
    return tupples


def find_element(matrix, element):
    row, col = 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if element == matrix[i][j]:
                row = i
                col = j

    return [row, col]


def playfair_encryption(plaintext, key):
    ciphertext = ''
    plaintext = plaintext.replace('j', 'i')
    key_matrix = create_matrix(key)
    tupples = create_tupples(plaintext)
    for i in tupples:
        if find_element(key_matrix, i[0])[0] == find_element(key_matrix, i[1])[0]:
            row = find_element(key_matrix, i[0])[0]
            col1 = (find_element(key_matrix, i[0])[1] + 1) % 5
            col2 = (find_element(key_matrix, i[1])[1] + 1) % 5
            ciphertext += key_matrix[row][col1] + key_matrix[row][col2]

        elif find_element(key_matrix, i[0])[1] == find_element(key_matrix, i[1])[1]:
            col = find_element(key_matrix, i[0])[1]
            row1 = (find_element(key_matrix, i[0])[0] + 1) % 5
            row2 = (find_element(key_matrix, i[1])[0] + 1) % 5
            ciphertext += key_matrix[row1][col] + key_matrix[row2][col]
        else:
            row1 = (find_element(key_matrix, i[0])[0])
            row2 = (find_element(key_matrix, i[1])[0])
            col1 = (find_element(key_matrix, i[0])[1])
            col2 = (find_element(key_matrix, i[1])[1])
            ciphertext += key_matrix[row1][col2] + key_matrix[row2][col1]
    return ciphertext

def playfair_decryption(ciphertext, key):
    plaintext = ""
    ciphertext = ciphertext.replace('j', 'i')

    key_matrix = create_matrix(key)
    tupples = create_tupples(ciphertext)
    for i in tupples:
        if find_element(key_matrix, i[0])[0] == find_element(key_matrix, i[1])[0]:
            row = find_element(key_matrix, i[0])[0]
            col1 = (find_element(key_matrix, i[0])[1] - 1) % 5
            col2 = (find_element(key_matrix, i[1])[1] - 1) % 5
            print(find_element(key_matrix, i[0]), find_element(key_matrix, i[1]))
            plaintext += key_matrix[row][col1] + key_matrix[row][col2]

        elif find_element(key_matrix, i[0])[1] == find_element(key_matrix, i[1])[1]:
            col = find_element(key_matrix, i[0])[1]
            row1 = (find_element(key_matrix, i[0])[0] - 1) % 5
            row2 = (find_element(key_matrix, i[1])[0] - 1) % 5
            plaintext += key_matrix[row1][col] + key_matrix[row2][col]
        else:
            row1 = (find_element(key_matrix, i[0])[0])
            row2 = (find_element(key_matrix, i[1])[0])
            col1 = (find_element(key_matrix, i[0])[1])
            col2 = (find_element(key_matrix, i[1])[1])
            plaintext += key_matrix[row1][col2] + key_matrix[row2][col1]
    return plaintext


pt = "jainilpatel"
key = "monarchy"
print("plaintext: ", pt)
ct = playfair_encryption(pt, "monarchy")
print("ciphertext: ", ct)
print("plaintext: ", playfair_decryption(ct, key))
