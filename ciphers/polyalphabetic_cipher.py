import string

def vig_enc(string, ks):
    cipher = ""
    for char in string:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            cipher += chr((ord(char) - base + ks) % 26 + base)
        else:
            cipher += char
    return cipher


def trans_enc(string, num_rows):
    rails = [""] * num_rows
    direction = 1  
    row = 0

    for char in string:
        rails[row] += char
        row += direction

        if row == num_rows - 1 or row == 0:
            direction *= -1

    return "".join(rails)


def encrypt(msg, caesar_ks, trans_rows):
    cs_cipher = vig_enc(msg, caesar_ks)
    trans_cip = trans_enc(cs_cipher, trans_rows)
    return trans_cip


def trans_dec(cipher, num_rows):
    rails = [""] * num_rows
    direction = 1
    row = 0

    for char in cipher:
        rails[row] += "*"
        row += direction

        if row == num_rows - 1 or row == 0:
            direction *= -1

    index = 0
    for i in range(num_rows):
        for j in range(len(rails[i])):
            rails[i] = rails[i][:j] + cipher[index] + rails[i][j + 1 :]
            index += 1

    string = ""
    direction = 1
    row = 0

    for i in range(len(cipher)):
        string += rails[row][0]
        rails[row] = rails[row][1:]
        row += direction

        if row == num_rows - 1 or row == 0:
            direction *= -1

    return string


def decrytp(cipher, caesar_ks, trans_rows):
    trans_deced = trans_dec(cipher, trans_rows)
    caesar_decrypted = vig_enc(trans_deced, -caesar_ks)
    return caesar_decrypted


msg = "The cargo leaves today with Colonel Kurt Hansen"
k = input("whats the key:")

key = int(string.ascii_lowercase.index(k))
rows = int(input("Rows to shift it by: "))

encrypted_msg = encrypt(
    msg, key, rows
)
print("ENcrypted msg:", encrypted_msg)

decrypted_msg = decrytp(
    encrypted_msg, key, rows
)
print("The secret is:", decrypted_msg)
