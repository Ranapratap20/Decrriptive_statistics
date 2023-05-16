class Atm:
    pin=None
    balance=0
    def __init__(self):
        print("Hi welcome to HDFC bank")
        self.pin=input("create a 4 digit pin")
        print("congrats your pin has been created")
    def checkBalance(self):
        temp=input("enter your 4 digit pin")
        if temp==self.pin:
            print("your current balance is ",self.balance)
        else:
            print("what is needed to know others balance") 
    def deposit(self):
        temp=input("Enter your 4 digit pin")
        if temp==self.pin:
            ammount=int(input("enter the amount"))
            self.balance=self.balance+ammount
            print("deposit sucessful")
        else:
            print("vosribala") 
    def withdraw(self):
        temp=input("enter your 4 digit pin")
        if temp==self.pin:
            ammount=int(input("enter the amount")) 
            if ammount<self.balance:
                self.balance=self.balance-ammount
                print("mil gaya bc")
            else:
                 print("akkad mein reh")
        else:
            print("sale chor")                               