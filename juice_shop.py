import random

class Customer:
    def __init__(self ,name  ):
        self.consumables  = {}
        self.name = name
        # self.token_no = token_no
        self.phone_no = None
    
    def __str__(self):
        return self.name


class Juice :
    def __init__(self ,flavour ,price):
        self.flavour = flavour
        self.price = price

    def __str__(self):
        return self.flavour + str(self.price)


# class Generate_Token :
#     def __init__(self ,customer):
#         # self.token_no = token_no
#         self.token_available = [x for x in range(1,50)]
#         self.token_occupied = []
#         self.customer = customer

#     def generate_token(self):
#         token = random.choice(self.token_available)
#         self.customer.token_no = token
#         self.token_available.remove(token)
#         self.token_occupied.append(token)
#         return token


class Generate_Bill :
    Token_No = 1
    def __init__(self ,customer ,juice):
        # self.name = name
        self.customer = customer
        self.juice = juice
        token_no = str(Generate_Bill.Token_No)
        self.token_no = "TKN"+"0"*(3-len(token_no))+token_no
        # print(self.token_no)
        Generate_Bill.Token_No += 1

    def bill(self):
        bill_str = f"Dear , {self.customer.name} your Token Number. is  {self.token_no}. \n"
         
        bill_str += (f"Your Juice: {self.juice.flavour} is getting prepared , \nand your total Cost is Rs.{self.juice.price} ")

        return bill_str
     


if __name__ == "__main__" :

    juice1 = Juice("Blackberry-Current", 80)
    juice2 = Juice("Kit-Kat-Shake", 100)
    

    customer1 = Customer("Namikaze")

    # token_generate1 = Generate_Token(customer1)
    # token_generate1.generate_token()
    bill1 = Generate_Bill(customer1, juice1)
    print_bill1 = bill1.bill()
    print(print_bill1 ,"\n")


    customer2 = Customer("Hatake_kakashi")
    # token_generate2 = Generate_Token(customer2)
    # token_generate2.generate_token()
    bill2 = Generate_Bill(customer2,juice2)
    print_bill2 = bill2.bill()
    print(print_bill2)