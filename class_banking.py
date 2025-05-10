class bank :
    bal = 10000
    def check_bal (self,bal ,deposit, withdraw):
        self.bal = bal
        self.deposite = deposit
        self.withdray = withdraw
        current_bal = bal + deposit - withdraw
        print(f'Current Balance in your account is {current_bal}.')
        self.bal = current_bal
        
        
    def Deposite(self, deposite):
        current_bal = deposite + self.bal
        print(f'You are Deposite amount is {deposite}.')
        print(f'Current Balance in your account is {current_bal}.')
        self.bal = current_bal
        
    def Withdraw(self, withdraw):
        current_bal =  self.bal - withdraw 
        print(f'You are withdraw amount is {withdraw}.')
        print(f'Current Balance in your account is {current_bal}.')
        self.bal = current_bal
        
        
def start():
    print('Welcome our ATM')
    sbi = bank()
    select = int(input("""\n1. Check Balance\n2. Deposite\n3. Withdraw\n"""))
    if select == 1:
        sbi.check_bal(bal= 10000, deposit= 0 , withdraw= 0)
    elif select ==2 :
        deposite = int(input("Enter your Deposite Money : "))
        sbi.Deposite(deposite)
    elif select ==3 :
        withdraw = int(input("Enter the Withdraw Amount : "))
        sbi.Withdraw(withdraw)
    
    