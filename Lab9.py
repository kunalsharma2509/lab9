#Nolan Hutyra
def encode(oldPass):
    tempList = []
    newPass = ""
    for item in oldPass:
        tempList.append(int(item))
    for item in tempList:
        if item <= 6:
            item += 3
            newPass += str(item)
        elif item > 6:
            item -= 7
            newPass += str(item)
    return newPass

def main():
    while True:
        print(f"Menu\n1. Encode\n2. Decode\n3. Quit")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            global passList
            passList = []
            password = input("Please enter your password to encode: ")
            passList.append(password)
            encodedPass = encode(password)
            passList.append(encodedPass)
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            print("Your encoded password is ", passList[1], ", and the original password is ", passList[0])
        elif choice == 3:
            break

if __name__ == "__main__":
    main()