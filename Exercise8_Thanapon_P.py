print("Welcome to Lz Shirt Shop.")
print("Please login for shop your shirt.")
print("--------------------")
usernameInput = input("Username : ")
passwordInput = input("Password : ")
print("--------------------")
if usernameInput == "admin" :
    if passwordInput == "password1234":
        print("Login success. Welcome to Lz Shirt Shop.")
        print("Shirt price list per size.")
        print("XS size: 179 THB.")
        print("S size: 199 THB.")
        print("M size: 219 THB.")
        print("L size: 239 THB.")
        print("XL size: 259 THB.")
        print("--------------------")
        size = input("What size you want? : ")
        if size == "XS" or size == "xs":
            noShirt = int(input("How many shirt you want? : "))
            print("Total price is:",179*noShirt,"THB.")
            print("Thank for shopping my Lz Shirt Shop.")
        elif size == "S" or size == "s":
            noShirt = int(input("How many shirt you want? : "))
            print("Total price is:",199*noShirt,"THB.")
            print("Thank for shopping my Lz Shirt Shop.")
        elif size == "M" or size == "m":
            noShirt = int(input("How many shirt you want? : "))
            print("Total price is:",219*noShirt,"THB.")
            print("Thank for shopping my Lz Shirt Shop.")
        elif size == "L" or size == "l":
            noShirt = int(input("How many shirt you want? : "))
            print("Total price is:",239*noShirt,"THB.")
            print("Thank for shopping my Lz Shirt Shop.")
        elif size == "XL" or size == "xl":
            noShirt = int(input("How many shirt you want? : "))
            print("Total price is:",259*noShirt,"THB.")
            print("Thank for shopping my Lz Shirt Shop.")
    else:
        print("Incorrect password.")
else:
    print("This username is not correct.")