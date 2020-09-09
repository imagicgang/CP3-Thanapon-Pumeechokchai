menuList = []
priceList = []
#-----------------------
def showBill():
    totalPrice = 0
    print("----- Your Bill -----")
    for number in range(len(menuList)):
        print(str(number+1)+".",menuList[number],priceList[number],"THB")
        totalPrice += int(priceList[number])
    print("Total price :",totalPrice,"THB")
#-----------------------
while True:
    menuName = input("Please Enter Menu. :")
    print("If you want to calculate overall, please type 'Exit'.")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Please Enter Price. :")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
