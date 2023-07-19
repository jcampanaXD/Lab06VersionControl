def encoder(password):
    encoded_pw = ""
    # iterate though password, adding 3 to each
    for i in password:
        added = str((int(i) + 3))
        # append to string
        encoded_pw += added
    # return string
    return encoded_pw


def decoder(encoded_pw):
    decoded_pw = ""
    # iterate through encoded pw, subrtacting 3 from each
    for i in encoded_pw:
        subtracted = str((int(i) - 3))
        decoded_pw += subtracted
    return decoded_pw


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print(" ")
        opt = int(input("Please enter an option: "))
        if opt == 1:
            password = input("Please enter your password to encode: ")
            encoded_pw = encoder(password)
            # encode
            print("Your password has been encoded and stored!")
        elif opt == 2:
            # decode
            decoded_pw = decoder(encoded_pw)
            print(f"The encoded password is {encoded_pw}, and the original password is {decoded_pw}.")
        elif opt == 3:
            break


if __name__ == "__main__":
    main()