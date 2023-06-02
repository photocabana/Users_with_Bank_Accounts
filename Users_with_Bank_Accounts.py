class User:
    def __init__(self, name, email):
        print(f"Welcome to EggShooter's Bank - Where all we think about is your nest egg!")
        self.name = name
        self.email = email
        self.accounts = {
            "chicken" : BankAccount(int_rate = 0.015, balance=0),
            "egg" : BankAccount(int_rate = 0.02, balance=0),
        }

    def make_deposit(self, amount, chicken):
        self.accounts[chicken].deposit(amount)
        return self

    def make_withdrawal(self,amount,egg):
        self.accounts[egg].withdrawal(amount)
        return self
    
    def display_user_balance(self,chicken):
        print(self.name)
        self.accounts[chicken].display_account_info()
        return self


class BankAccount:
    print(f"Welcome to EggShooter's Bank - Where all we think about is your nest egg!")
    account_list = []

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.account_list.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdrawal(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
        
    def display_account_info(self):
        print(f"Your current balance is {self.balance}")
        return self
        
    def yield_interest(self):
        if self.balance >= 0:
            print(f"Your current interest rate is {self.int_rate}")
        return self
    
    # def transfer(self, amount, account):
    #     self.balance = self.balance - amount
    #     # name.balance = name.balance + amount
    #     return self

    @classmethod
    def all_accounts(cls):
        for account in cls.account_list:
            account.display_account_info()


account1=BankAccount(0.01,250)
account1.yield_interest().deposit(300).deposit(20).display_account_info().deposit(55).withdrawal(275)
account2=BankAccount(0.0098,465)
account2.deposit(400).deposit(942).withdrawal(57).withdrawal(520).withdrawal(600).yield_interest().display_account_info()


user1 = User("Rindy", "rinnn16@hotmail.com")
user1.make_deposit(100,"egg").make_deposit(250,"chicken").make_withdrawal(75,"chicken").display_user_balance("chicken")

user2 = User("Michael", "vinnarrk@hotmail.com")
user2.make_deposit(1000, "chicken").make_withdrawal(450, "chicken").display_user_balance("chicken")
# user1.transfer(100, user2,"egg")

# user3 = User("Mr Moneybags", "moneyMoneyMoney@$$$$.org")
# user3.make_deposit(150000000).user1_name_balance(85000).display_user_balance()

# user4 = User("Miss Moolaa", "IHaveAYacht@DontYouWishYouWereMe.com")
# user4.make_deposit(8675309).user2_name_balance(52000).display_user_balance()
