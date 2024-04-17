class BankAccount:
    ''' when we create a new account we should have initial amount and the namr of the account  '''
    
    def __init__(self , initial_amount , account_name):
        self.balance = initial_amount
        self.name = account_name
        print(f"\nAccount '{self.name}' is created successfully 😊\nYour Balance Is : {self.balance:.2f} EGP")
    def get_balance(self):
        print(f"\nYour Account Name Is '{self.name}'\nYour Balance Is : {self.balance} EGP")
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit completed 😊")
        self.get_balance()
        
    def withdraw(self, amount):
        if self.balance >= amount:
            print("\nWithdraw completed 😊")
            self.balance = self.balance - amount
            self.get_balance()
        else:
            raise Exception(f"\nSorry , Process Not Completed\nYour Balance Is : {self.balance} EGP")