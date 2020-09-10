systemMenu = {"ข้าวหมกไก่":45,"ข้าวมันไก่":40,"ข้าวมันไก่ผสม":50,"ข้าวมันไก่พิเศษ":45,"ข้าวมันไก่ทอด":40}
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
        print("Menu List.")
        for j in systemMenu.items():
            print(j)            
        print(">>If you want to calculate overall, please type 'Exit'.<<")
        print("--------------------")
    menuName = input("Please Enter Menu. :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
        print("--------------------")
#-----------------------
showBill()