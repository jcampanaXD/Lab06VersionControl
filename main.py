# Joelie Campana and Hunter Stewart
def encoder(password):
    encoded_pw = ""
    # iterate though password, adding 3 to each
    for i in password:
        added = str((int(i) + 3) % 10)
        # append to string
        encoded_pw += added
    # return string
    return encoded_pw


def decoder(encoded_pw):
    encoded_pw = [int(num) for num in list(encoded_pw)]  # password into integer list
    for idx, num in enumerate(encoded_pw):
        decoded_num = encoded_pw[idx] - 3
        if decoded_num < 0:
            remainder = 10 + decoded_num  # takes amount below 0
            encoded_pw[idx] = remainder  # replaces value out of range, with new in value range
        else:
            encoded_pw[idx] -= 3
    decoded_pw = ''.join([str(num) for num in encoded_pw])  # decoded password put back into string
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
            decoded_pw = decoder(encoded_pw)
            print(f"The encoded password is {encoded_pw}, and the original password is {decoded_pw}.")
        elif opt == 3:
            break


if __name__ == "__main__":
    main()