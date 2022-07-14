def letters():
    letters_bank = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                    'z']
    return letters_bank

def ceasar_cipher_encryption(my_string, key):
    split_string = list(my_string)
    # print(''.join(split_string))
    encrypted_word = []
    for i in range(len(split_string)):
        for j in range(len(letters())):
            if split_string[i] == letters()[j]:
                length = len(letters())
                ciphered_letter = letters()[(j+key) % length]
                encrypted_word.append(ciphered_letter)
    print(''.join(encrypted_word))

def ceasar_cipher_decryption(my_string, key):
    split_string = list(my_string)
    # print(''.join(split_string))
    encrypted_word = []
    for i in range(len(split_string)):
        for j in range(len(letters())):
            if split_string[i] == letters()[j]:
                length = len(letters())
                ciphered_letter = letters()[(j-key) % length] #find the mod to avoid index_error
                encrypted_word.append(ciphered_letter)
    print(''.join(encrypted_word))

def main():
    choice = input("Press 1 for Encrypt\nPress 2 for decrypt\n")
    my_word = input("What is your word? ")
    my_key = int(input("What is your key? "))
    if choice == '1':
        print("Encrypted word: ")
        ceasar_cipher_encryption(my_word, my_key)
    elif choice == '2':
        print("Decrypted word: ")
        ceasar_cipher_decryption(my_word, my_key)
    else:
        print("Huh?")

if __name__ == '__main__':
    main()
