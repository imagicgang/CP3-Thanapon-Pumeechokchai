number = int(input("Input your number of asterisk pylamid line.: "))
asterisk = "*"
for loop in range(number):
    number -= 1
    print((" "*number)+(((2*loop)+1)*asterisk))