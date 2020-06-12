class Customer:
    name = ""
    lastname = ''
    age = 0

    def addcart(self):
        print('added to',self.name,self.lastname, 'cart')

customer1 = Customer()
customer1.name = 'bread'
customer1.lastname = 'bun'
customer1.addcart()

customer2 = Customer()
customer2.name = 'patranun'
customer2.lastname ='chinsakchai'
customer2.addcart()

customer3 = Customer()
customer3.name = 'pakanun'
customer3.lastname = 'chinsakchai'
customer3.addcart()

customer4 = Customer()
customer4.name = 'lat'
customer4.lastname = 'te'
customer4.addcart()