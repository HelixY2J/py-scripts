# The string to be encrypted/decrypted:
message = input("> Enter the message:\n")



# The encryption/decryption key:

key = int(input(">enter the key \n: "))

 # Whether the program encrypts or decrypts:



print(">  Set to either 'encrypt' or 'decrypt")

mode = input("")

 # Every possible symbol that can be encrypted:

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

 # Store the encrypted/decrypted form of the message:

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode == 'encrypt':
            t_index = symbolIndex + key
        elif mode == 'decrypt':
            t_index = symbolIndex - key

        # handling wrapround 

        if (t_index >= len(SYMBOLS)):
            t_index = t_index - len(SYMBOLS)
        elif t_index < 0:
            t_index = t_index + len(SYMBOLS)

        translated = translated + SYMBOLS[t_index]

    else:
        # append it without encrpting/decryting
        translated = translated + symbol


print(translated)
