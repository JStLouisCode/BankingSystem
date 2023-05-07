# BankingSystem
This is a Python program for a simple banking system that allows users to perform basic banking functions such as deposit, withdrawal, check balance, and online banking setup.

## How to Use the Program

1. Create a BankAccount object by defining the user's name, age, and address.
2. Set up online banking by calling online_banking_setup() function, which will prompt the user to enter their username and password.
3. Log in to the account by calling online_login() function, which requires the user to enter their username and password.
4. Once logged in, the user can perform banking functions such as deposit, withdrawal, check balance, add a new contact, view the contact list, send money, and log out.
5. When done, the user can log out of the account by calling the logout() function.

## Functions
Here are the details of the functions available in this program:

### '__init__(self, name: str, age: int, address: str) -> None'
This is the constructor method that initializes the object with the user's name, age, and address. It also sets the user's balance to zero and creates variables to store the user's login credentials, online banking setup status, and contact list.

# 'online_banking_setup(self)'
This function sets up online banking for the user by asking them to enter their username and password. It can only be done once per account.

# 'online_login(self, username: str, password: str)'
This function logs the user into their account by checking their username and password against the ones previously entered during online banking setup.

# 'withdrawal(self, amount: int) -> int'
This function allows the user to withdraw money from their account. It checks if the user is logged in, and if so, it updates their account balance. If the withdrawal amount is greater than the available balance, it displays an error message.

# 'deposit(self, amount: int) -> int'
This function allows the user to deposit money into their account. It checks if the user is logged in and updates their account balance.

# 'check_balance(self) -> int'
This function allows the user to check their current account balance. It checks if the user is logged in and displays their current balance.

# 'add_contact(self, password: str)'
This function allows the user to add a new contact to their account. It prompts the user to enter a password for security purposes before allowing them to enter the new contact's name and phone number.

# 'show_contacts(self)'
This function displays the user's contact list in alphabetical order.

# 'send_money(self)'
This function allows the user to send money to a contact in their list. It first checks if the contact exists in the user's list and prompts the user to add it if it doesn't. Then it prompts the user to enter the amount they wish to transfer. If the amount is greater than the available balance, an error message is displayed.

# 'logout(self)'
This function logs the user out of their account. It sets their login status to False and displays a message confirming the logout.

# Conclusion
This program provides basic banking functionality and can be customized further to meet more specific needs.
