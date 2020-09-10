menuList = []
i = 0
#-----------------------
def showBill():
    totalPrice = 0
    print("----- Your Bill -----")
    for number in range(len(menuList)):
        print(str(number+1)+".",menuList[number][0],menuList[number][1],"THB")
        totalPrice += int(menuList[number][1])
    print("Total price :",totalPrice,"THB")
#-----------------------
while True:
    i += 1
    if i == 1:
        print("---------- AXY Resturant. ----------")
        print(">>If you want to calculate overall, please type 'Exit'.<<")
        print("--------------------")
    menuName = input("Please Enter Menu. :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Please Enter Price. :")
        menuList.append([menuName,menuPrice])
        print("--------------------")
#-----------------------
showBill()