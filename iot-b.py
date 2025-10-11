# To create the BankAccount class
class bank:
    def __init__(self):
      self.bal = 0 #Initialize balance to 0
      print("Welcome to the SBI")

    def deposit(self):
        amt = float(input("Enter amount to be Deposited: "))
        self.bal+=amt
    def withdraw(self):
      amt = float(input("Enter amount to be Withdrawn:"))
      if self.bal>=amt:
         self.bal_=amt
         print("\nWithdrew:",amt)
      else:
         print("\nInsufficent balance")
         
    def display(self):
      print("\nNet Avaliable Balance=",self.bal)
      

#driver code
s = bank() #create an object of BankAccount

s.deposit()    #Deposit money
s.withdraw()    #Withdraw money
s.display()      #Display balance

      
