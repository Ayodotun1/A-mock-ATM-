#REGISTER FUNCTION
# USERNAME, PASSWORD, EMAIL ADDRESS
#GENERATE ACCOUNT NUMBER, USE ACCOUNT NUMBER AS ID, CREATE A PASSWORD

#LOGIN FUNCTION
#ACCOUNT ID OR EMAIL, PASSWORD
#REQUEST FOR STATEMENT OF ACCOUNT

database = {}
def_balance = 0

import numpy as np
import random

def init():
    print('WELCOME TO DEE BANK\n')
    option = False
    while option ==False:
        print('Do you have a bank account with us?\n') 
        acc = input('Yes or No?\ Y or N\n')
        if acc == 'Y':
            option = True
            login()
        elif acc == 'N':
            option = True
            opt = False
            while opt == False:
                print('Do you want to register a bank account with us?\n')
                reg = input('Yes or No?\ Y or N\n')
                if reg == 'Y':
                    opt = True
                    register()
                    ID_gen()
                    login()
                elif reg == 'N':
                    opt = True
                    exit()
                else:
                    print('Kindly select a valid option\n')
        else:
            print('Kindly select a valid option\n')

def acccountnumber():
    print('\nGenerating Account Number...\n')
    return random.randrange(1111111111, 9999999999)

def accountID():
    print('Generating Account ID.....\n\n')
    chars = np.array(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ0123456789'))
    np_codes = np.random.choice(chars,10)
    print(''.join([val for val in np_codes]))
    print('\n')

def ID_gen():
    data = database
    opt = False
    while opt == False:
        ID = input("\nDo you have a user ID?\nYes or No\nY or N\n")
        if ID == 'Y':
            opt = True
            login()
        elif ID == 'N':   
            opt = True
            y = input('Enter your account number to generate your unique UserID to enable login functionality\n')
            pin2 = input('Enter your 4 digit pin\n')
            for x,pin in database.items():
                if (acccountnumber == y):
                    if (pin[2] == pin2):
                        accountID()
                    else:
                        print('Invalid account number or pin')
        else:
            print('Kindly select a valid option')

def register():
    name = input('\nKindly fill in your name in the following order:\nFirst Middle Last\n')
    email_address = input('\nKindly input your valid and functional email address below\n')
    opt = False
    pin = input('\nEnter your desired pin\n')
    x = acccountnumber()
    print(f'{x} is your account number')
    database [x] = [ name, email_address, pin]
    return database



def login():
    print("Welcome to our Login Page")

    account = (input("What is your account number? \n"))
    password = input("What is your password \n")

    if (accountNumber,userDetails) in database.items():
        if(accountNumber == account):
            if(userDetails[3] == password):
                bankOperation(userDetails)
                operation()
            else:
                print('')
        else:
            print('')
                
    else:
        print('Invalid account or password')

def withdrawal():
    while True:
        try:
            amount = int(input('How much would you like to withdraw?\n'))
        except ValueError:
            print('Insert amount, not lett5ers.... Else e go choke o\n\n')
            continue
        break
    if amount > def_balance:
		     print('Insufficient funds....\n')
    elif amount <= def_balance:
        current_balance = def_balance - amount
        print('Transaction Processing......\n\n')
        print('Take your cash\n')

def deposit():
 while True:
    try:
        amount = int(input('How much would you like to deposit?\n'))
    except ValueError:
        print('You can only deposit numbers bro')
        continue
    break
    current_balance = amount + def_balance
    print('Transaction Processing...\n\n')
    print('DONE!!!\n')
    print(f'Dear {database[x][0]}, your current account balance is {current_balance}\n')
   
def complaint():
    print(f'Thank you for reaching out to us, dear customer. \n\nWe are here to serve you and give you the best banking experience ever\n')
    print('What issue will you like to report?\n\n')
    input('')
    print('\n\n')
    print('Thank you for contacting us')


def operation():
    action = int(input('What do you want to do?\n1. Withdrawal 2. Deposit 3. Complaint'))
    if action == 1:
        withdrawal()
    elif action == 2:
        deposit()
    elif action == 3:
        complaint()
    else:
        print('Enter a valid option')

def exit():
    print('Bye, Thank you for banking with us')
init()