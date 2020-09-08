def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
x = int(input("Input your Price: "))
print("Total price is",vatCalculate(x),"THB")
