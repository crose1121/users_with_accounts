class User():
    def __init__(self,name):
        self.account = Bank_Account(1.04, "Checking", 10000)
        self.name = name
        self.account_names = {self.account.name:self.account}

    def create_account(self,name,rate,balance=0):
        new_account = Bank_Account(int_rate=rate,balance=balance,name=name)
        self.account_names[new_account.name] = new_account
        return self

    def make_deposit(self,amount,name): #
        self.account_names[name].deposit(amount)
        return self
    
    def make_withdrawal(self,amount,name): #
            self.account_names[name].withdraw(amount)
            return self

# #Does transfer_money() belong in User Account or Bank Account class? It seems like conditionals being used to control whether or not withdrawals can happen. Encapsualtion makes me feel like this belongs in the Bank Account class.
    def transfer_money(self,other_user,amount): 
        self.other_user = other_user
        self.amount = amount
        if self.account.balance >= amount:
            self.account.make_transfer(other_user,amount)
            self.account.balance -= amount        
            # These two lines (20 and 21) have been placed in the Bank Account method make_transfer() instead.
#             # other_user.account.balance += amount  
#             print("Your money has been transferred")
#             # return self #I switched the functionality of the transfer method to the Bank Account class - do I return self there instead? I think yes.
#         else:
#             print("Insufficient Funds!")

    def interest(self): 
        self.account.yield_interest()


    def display_user_balance(self): #Does this belong in User class or Bank Account class?
        print(f"Name: {self.name}\nAccount Balance: {self.account.balance}")


class Bank_Account:
    all_accounts = []

    def __init__(self,int_rate,name,balance=0):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        Bank_Account.all_accounts.append(self)

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        self.balance -= amount
        return self

    def make_transfer(self,other_user,amount): 
        self.other_user = other_user
        self.amount = amount
        if self.balance >= amount:
            
            self.balance -= amount        #These two lines (20 and 21) have been placed in the Bank Account method make_transfer() instead.
            other_user.account.balance += amount  
            print("Your money has been transferred")
            return self                 #Should I return self here? I think yes.
        else:
            print("Insufficient Funds!")
    
    def display_balance(self): #Does this belong in User class or Bank Account class? Do we need two of these?
        print(f"Your balance is: {self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance = round((self.int_rate * self.balance),2)
            return self
        else:
            print("Account has a negative balance")

    @classmethod
    def print_account_info(cls):
        sum = 0
        for item in cls.all_accounts:
            sum += item.balance
        return sum 

user1 = User("Corey")
user2 = User("Tyler")
user3 = User("Rose")

# user1.account.display_balance() #Not sure which of these I should be using?
user3.display_user_balance() #Not sure which to use

#Deposit is a User class behavior. Are we using the make_deposit method from the User Class to perform this behavior, or are we using the deposit method from the Bank_Account class? If we are using the deposit method from the Bank Account Class, why do we even need the make_deposit function or make_withdrawal function at all in the User Class? See below too.

user1.make_deposit(4000).make_deposit(1000).make_deposit(500).make_withdrawal(200).interest()
user1.display_user_balance()

user2.make_deposit(1000).make_deposit(900).make_withdrawal(500).make_withdrawal(200).display_user_balance()

user3.make_deposit(2000).make_withdrawal(3000).make_withdrawal(2000).make_withdrawal(2000).display_user_balance()

user2.display_user_balance()
user1.transfer_money(user2,1500)
user2.display_user_balance()

print(Bank_Account.print_account_info()) #This is finally working!

#How to have a user with multiple user accounts?
#BAM! Donezo.

user1.create_account("Retirement",1.03,1000)
print(user1.account_names)