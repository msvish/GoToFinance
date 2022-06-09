class Account:
    def __init__(self):
        self.dollar=0
        self.cents=0
        self.menu()
        
    def credit(self,creditAmount):
        pass
    
    def debit(self,debitAmount):
        pass
    
    def checkBalance(self):
        print("Balance:\t"+"{}D {}C".format(self.dollar,self.cents))
        
    def menu(self):
        current=True

        while(current):
            print("What would you like to do: \n {}. Credit \n {}. Debit \n {}. Check Balance \n {}. Exit \n".format(1,2,3,4))
            option=int(input("Please select your option"))
            if option==1:
                amount=str(input("Enter the amount "))
                self.credit(amount)
            elif option==2:
                amount=str(input("Enter the amount "))
                self.debit(amount)
            elif option==3:
                self.checkBalance()
                print("\n")
            elif option==4:
                print("Thank you! \n")
                current=False
            else:
                print("Invalid option \n")
                
Account()
