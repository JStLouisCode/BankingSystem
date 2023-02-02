#Jared St.Louis

#Banking System

#Imports
import time


#Parent Class
class BankAccount:
    #Function Definitions
    
    def __init__(self, name: str, age: int, address: str) -> None:      
        self.balance = 0
        self.name = name
        self.age = age
        self.address = address
        self.username = None
        self.password = None
        self.online_banking_setup = False
        self.login = False
        self.contacts = {}
        
        
    def onine_banking_setup(self):
        if self.online_banking_setup == False:
            self.username = input("Please enter your username: ")
            self.password = input("Please enter your password: ")
            self.online_banking_setup = True
        else:
            print("Your online banking is already setup.")
            
            
    def online_login(self, username: str, password: str):
        if (username == self.username and password == self.password):
            self.login = True
            print("Successfully logged in.")
        else:
            print("Your username or password is incorrect, please try again!")
            
            
    def withdrawal(self, amount: int) -> int:
        """
        Return the bank balance of the user after they've decided to take money out.
        amount is the number in $ that user would like to deposit.
        """
        if self.login:
            self.amount = amount
            if self.amount > self.balance:
                print("Insufficient funds. ")
                print("Account Balance: $", self.balance)
            else:
                self.balance = self.balance - self.amount
                print("Account balance updated: $",self.balance)
        else:
            print("Please login before attempting withdrawal")
            
            
    def deposit(self, amount: int) -> int:
        """
        Return the bank balance of the user.
        amount is the number in $ that user would like to deposit.
        """
        if self.login:
            self.amount = amount
            self.balance = self.balance + self.amount
            print("Account balance updated: $", self.balance)
        
        
    def check_balance(self) -> int:
        """
        Return amount of $ in user's account.
        """
        if self.login:
            print("Account Balance: $", self.balance)
        
        
    def add_contact(self, password: str):
        """
        Returns an added NEW contact to the account. 
        
        password is the string that mimics 2FA required, before adding a new contact.
        """
        if self.login:
            self.password = input("Please enter your password: ")
            if password == self.password:
                name = input("Enter the persons name: ")
                print("")
                number = str(input("Enter the persons phone number: "))
                self.contacts[name] = number
                print(f"{name} with phone numer {number} added to contacts.")
            else:
                self.password = input("Please enter your password: ")
            
    #function for displaying contact list
    def show_contacts(self):
        """
        Returns a sorted list of contacts, previously added to the list.
        """
        if self.login:
            keys = list(self.contacts.keys())
            n = len(keys)
        
            #Bubble Sort Algo
            for i in range(n):
                for j in range(0, n-i-1):
                    if keys[j] > keys[j+1]:
                        keys[j], keys[j+1] = keys[j+1], keys[j]
                    
            print("Sorted Contact List:")
            for key in keys:
                print(key, ":", self.contacts[key])   
            
            
    def send_money(self):
        if self.login:
            contact_name = input("Who would you like to send money to?") 
            contact_found = False
            # check if contact is already in contact list
            for name in self.contacts.keys():
                if name == contact_name:
                    contact_found = True
            
            # if contact is not in contact list
            if contact_found == False:
                self.add_contact()
                
            transfer_amount = input("How much do you want to transfer") 
            if transfer_amount > self.balance:
                print("Insufficient funds. ")
                time.sleep(5)
                print("Account Balance: $", self.balance)
            else:
                self.balance = self.balance - self.amount 
                print("Amount of",self.amount,"has been sent to", {name})
                time.sleep(5)
                print("Account balance updated: $",self.balance) 
                
    def logout(self):
        
        self.login = False
        print("You have been successfully logged out.") 

Richard_BA = BankAccount("Richard Hamilton", 32, "223 Webb Dr")
Richard_BA.onine_banking_setup()
Richard_BA.online_login("richard", "ajdjfahfaeil")
Richard_BA.withdrawal(10)
#Richard_BA.add_contact()