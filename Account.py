class Account:
    def __init__(self):
        self.dollar=0
        self.cents=0
        self.menu()
        
    def credit(self,creditAmount):
        amount=list(map(str,creditAmount.split(" ")))
        if len(amount)==2:
            dollarAmt=int(amount[0][:-1])
            centAmt=int(amount[1][:-1])
            self.dollar+=dollarAmt
            if(centAmt<0):
                self.cents=(self.cents+100)+centAmt
                self.dollar-=1
            else:
                self.cents+=centAmt
        else:
            if(amount[0][-1]=="D"):
                dollarAmt=int(amount[0][:-1])
                self.dollar+=dollarAmt
            else:
                centAmt=int(amount[0][:-1])
                if(centAmt<0):
                    self.cents=(self.cents+100)+centAmt
                    self.dollar-=1
                else:
                    self.cents+=centAmt
        if(self.cents>=100):
            self.cents-=100
            self.dollar+=1 
    
    def debit(self,debitAmount):
        amount=list(map(str,debitAmount.split(" ")))
        if len(amount)==2:
            dollarAmt=int(amount[0][:-1])
            centAmt=int(amount[1][:-1])
            self.dollar-=dollarAmt
            if(self.cents<centAmt):
                self.cents=(self.cents+100)-centAmt
                self.dollar-=1
            else:
                self.cents-=centAmt
        else:
            if(amount[0][-1]=="D"):
                dollarAmt=int(amount[0][:-1])
                self.dollar-=dollarAmt
            else:
                centAmt=int(amount[0][:-1])
                if(self.cents<centAmt and self.dollar!=0):
                    self.cents=(self.cents+100)-centAmt
                    self.dollar-=1
                elif(self.cents<centAmt and self.dollar==0):
                    self.cents=self.cents-centAmt
                    if self.cents<=-100:
                        self.cents+=100
                        self.dollar-=1
                else:
                    self.cents-=centAmt
        if(self.cents>=100):
            self.cents-=100
            self.dollar+=1 
    
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
