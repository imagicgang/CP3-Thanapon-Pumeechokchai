#----------------------------------------------------Space for announce function.
def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showManu()
    else:
        print("Please login again.")
        print("--------------------")
        return login()
def showManu():
    print("---- Jercy shop ----")
    print("Please select menu.")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return manuSelect()
def manuSelect():
    userSelect = int(input(">> "))
    if userSelect == 1:
        return vatCalculate(int(input("Input your price: ")))
    elif userSelect == 2:
        return priceCalculate()
    else:
        print("Please select again.")
        print("--------------------")
        return manuSelect()
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice*vat/100)
    print("--------------------")
    return "Total price is "+str(result)+" THB"
def priceCalculate():
    price1 = int(input("First Product price : "))
    price2 = int(input("Second Product price : "))
    return vatCalculate(price1+price2)
#----------------------------------------------------Space for write program. 
print("Please login to Price Calculator Program.")
print("--------------------")
print(login())
print("Thank for using program.") 
print("--------------------")