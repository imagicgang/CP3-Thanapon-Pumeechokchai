class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Add to "+self.name+" "+self.lastname+"'s cart.")

customer1 = Customer()
customer1.name = "Kai"
customer1.lastname = "Havertz"
customer1.addCart()

customer2 = Customer()
customer2.name = "Jadon"
customer2.lastname = "Sancho"
customer2.addCart()

customer3 = Customer()
customer3.name = "Leonel"
customer3.lastname = "Messi"
customer3.addCart()

customer4 = Customer()
customer4.name = "Mohamed"
customer4.lastname = "Salah"
customer4.addCart()

