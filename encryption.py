import random

def task4():
    # Create empty list of user and passwords
    user_list = []
    password_list = []

    # Ask how many users
    num_of_users = int(input("How many users would you like to add? "))

    # Call functions that create list of users and passwords
    list_users = create_user_list(num_of_users)
    list_passwords = create_password_list(list_users)

    # Create dictionary
    encrypted_username_password_combo = create_dictionary(list_users, list_passwords[1])
    username_password_combo = create_dictionary(list_users, list_passwords[0])

    # Display list of users and passwords
    print("List of users: {}".format(list_users))
    print("List of passwords: {} ---encryption---> {}".format(list_passwords[0], list_passwords[1]))

    # Display dictionary
    print("-- Displaying username/password combination --")
    print(username_password_combo)
    print("**ENCRYPTED** Displaying username/password combination **ENCRYPTED**")
    print(encrypted_username_password_combo)

    # Initiate login
    login_procedure(username_password_combo, encrypted_username_password_combo)

def character_pool():
    pool = ['a', ' ', 'S', 'b', 'Z', '!', 'c', '5', '@', 'd', 'e',
            'f', '#', 'T', 'g', 'R', '$', 'M', '4', 'h', '6', 'I', '%', 'i',
            '^', 'j','&', 'U', 'k', 'Y', 'Q', '*', '3', 'J', 'N', 'l', '(',
            'm', 'H', "'", '7', 'E', ')', 'n', 'D', '0', '-', 'o',
            'p', 'V', 'X', '_', '2', 'L', 'q', 'K', 'O', '=', 'r', 'G',
            '+', 's', '8', 'C', '<', 't', '>', ',', 'W', '1', 'P', '.', 'u',
            'v', '/', 'w', '?', 'F', 'x', '9', 'B', 'y', 'A', 'z']
    random.shuffle(pool)
    return pool

SHUFFLE_POOL = character_pool()
R = random.randint(1,len(character_pool()) - 1)

def cipher_encryption(string, shift, pool):
    list_encrypted_string = []
    for j in range(len(string)):
        for k in range(len(pool)):
            for i in string[j]:
                if i == pool[k]:
                    my_letter = pool[(k - shift) % len(pool)]
                    list_encrypted_string.append(my_letter)
                    break
    encrypted_string = ''.join(list_encrypted_string)
    return encrypted_string, shift

def cipher_decryption(string, shift, pool):
    list_decrypted_string = []
    for j in range(len(string)):
        for k in range(len(pool)):
            for i in string[j]:
                if i == pool[k]:
                    my_letter = pool[(k + shift) % len(pool)]
                    list_decrypted_string.append(my_letter)
                    break
    decrypted_string = ''.join(list_decrypted_string)
    return decrypted_string

def create_dictionary(list1, list2):
    username_password = dict(zip(list1, list2))
    return username_password

def create_user_list(number):
    user_list = []
    for i in range(number):
        user_input = input("Input a name: ")
        user_list.append(user_input)
    return user_list

def create_password_list(list_of_users):
    password_list = []
    encrypted_password_list = []
    for i in range(len(list_of_users)):
        password_input = input("Input password for {}: ".format(list_of_users[i]))
        pass_encrypt = cipher_encryption(password_input, R, SHUFFLE_POOL)[0]
        password_list.append(password_input)
        encrypted_password_list.append(pass_encrypt)
    return password_list, encrypted_password_list


def login_procedure(my_dict, encrypted_dict):
    print("WARNING: You are accessing a government site.")
    while True:
        login_name = input("Please enter username: ")
        for i in my_dict.keys():
            if login_name == i:
                for i in range(3):
                    type_password = input("Password: ")
                    if type_password == cipher_decryption(encrypted_dict[login_name], R, SHUFFLE_POOL):
                        print("Welcome, {}!".format(login_name))
                        print("Username/password combinations: {}".format(encrypted_dict))
                        pass_choice = input("Would you like to change your password? ").upper()
                        if pass_choice == 'YES' or pass_choice == 'Y':
                            new_password = input("Please input new password: ")
                            print("*OLD* Username/password combinations: {}".format(my_dict))
                            my_dict[login_name] = new_password

                            list_users = []
                            for i in my_dict.keys():
                                list_users.append(i)

                            new_encrypted_list = []
                            for i in my_dict.values():
                                new_encrypted_list.append(cipher_encryption(i, R, SHUFFLE_POOL)[0])
                            new_dict = create_dictionary(list_users, new_encrypted_list)
                            print("*UPDATED* Username/password combinations: {}".format(my_dict))
                            print("**ENCRYPTED** Username/password combinatoins: {}".format(new_dict))
                            print("Goodbye, {}!".format(login_name))
                            choice = input("Would you like to log in with another user? ").upper()
                            if choice == "YES" or choice == 'Y':
                                login_procedure(my_dict, new_dict)
                            return
                        else:
                            print("User has decided to not change password")
                            print("Have a good day!")
                            return
                    else:
                        print("Wrong password. Please try again.")
                print("Login failure. Self destruct sequence activated! lol")
                return
        else:
            print("User name not found. Try again.")

def main4():
    task4()

################################################################################
main4()
