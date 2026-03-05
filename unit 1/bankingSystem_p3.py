class NavyFedralNavy:
    def _init_(self, name, age, balance, accountNumber, phone, ):
        self.name = name 
        self.age = age
        self.balance = balance
        self.accountNumber = accountNumber
        self.phone = phone

    def deposit(self, balance, amount):
        balance +=amount
        print('you have'+ str (self.balance))

    def withdraw(self, balance,amount):
        balance -= amount
        print('you have '+ str (balance))

    def checkBalance(self):
        print('you have '+ str (self.balance))

account_1 = 'NavyFedralBank'("Bob", 45, 30, '124ab34', 'NA')
account_2 = 'NacyFedralBank'("stacy", 25, 100, '154av34', 'NA')

account_1.checkBalance()
account_2.checkBalance(500)
account_1.withdraw(150)

account_2.checkBalance()
account_2.deposit(500)
account_2.withdraw(150)

def createAccount():
    print("Welcome to NavyFedralBank")
    print("Please complete the form to create an account.")
    name = input ("please type in your name: ")
    age = int(input("please type in your age: "))
    balance = int(input("please type in how much you want to deposit: "))
    accountNumber = "random".ranrange(100,900)

    print("congrats your account is now complete")

    account = 'NavyFedralBank' (name, age, balance, accountNumber, 'na')

    "bankUser".append(account)

createAccount()

print("bankUser")