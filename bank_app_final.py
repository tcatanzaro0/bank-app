## Tucker Catanzaro
# Added it so that the program will search for an accounts.csv in the CWD. If one is found it will create the accounts dictionary from the file.
# If one is not found it will create the dictionary with the default values as shown below but when the user ends the program it will write the current dictionary to a .csv file named accounts.


import csv
import os.path
from tkinter import *

# Deposit, withdraw, or transfer
def menu():
	print("The current account standings are: ")
	print(accounts)
	print()
	print("Would you like to \n1. Deposit money \n2. Withdraw money \n3. Transfer money \n4. New account \n5. Quit")
	answer = input("Please enter the number of your choice. \n> ")
	if int(answer) == 1:
		deposit()
	elif int(answer) == 2:
		withdraw()
	elif int(answer) == 3:
		transfer()
	elif int(answer) == 4:
		create_account()
	elif int(answer) == 5:
		print("Thank you for choosing CS109 Credit Union!")
		w = csv.writer(open("accounts.csv", "w"))
		for key, val in accounts.items():
			w.writerow([key, val])
		return()
	elif answer > 5:
		print("You have entered an invalid choice, returning you to the menu.")
		menu()

# Deposit money
def deposit(name, amount):
	# deposit_account_name = input("Which account would you like to deposit money into (Case sensitive): ")
	# deposit_amount = int(input("How much would you like to deposit: "))
	if name in accounts:
		deposit_new_amount = str(int(accounts[name]) + deposit_amount)
		accounts[name] = deposit_new_amount
		print (accounts)
		end()
	else:
		print()
		print("Invalid entry, returning you to the menu.")
		menu()

#Withdraw money
def withdraw():
    withdraw_account_name = input("Which account would you like to withdraw money from (Case sensitive): ")
    withdraw_amount = int(input("How much would you like to withdraw: "))
    withdraw_new_amount = str(int(accounts[withdraw_account_name]) - withdraw_amount)
    if int(withdraw_amount) > int(accounts[withdraw_account_name]):
        print("This withdrawal would put the account into the negative. \nWe will now return you to the menu.\n")
        menu()
    elif int(withdraw_amount) <= int(accounts[withdraw_account_name]):
        accounts[withdraw_account_name] = withdraw_new_amount
        print("You have withdrawn $" + str(withdraw_amount) + " dollars.")
        print(accounts)
        end()

#Transfer money
def transfer():
    transfer_donor = input("Which account would you like to transfer money from (Case sensitive): ")
    transfer_recip = input("Which account would you like to transfer money to (Case sensitive): ")
    transfer_amount = int(input("How much would you like to transfer: "))
    transfer_donor_amount = str(int(accounts[transfer_donor]) - transfer_amount)
    transfer_recip_amount = str(int(accounts[transfer_recip]) + transfer_amount)
    if int(transfer_amount) > accounts[transfer_donor]:
        print("This transfer would put the account into the negative. \nWe will now return you to the menu.\n")
        menu()
    elif int(transfer_amount) <= int(accounts[transfer_donor]):    
        accounts[transfer_donor] = transfer_donor_amount
        accounts[transfer_recip] = transfer_recip_amount
        print()
        print("You have transferred $" + str(transfer_amount) + " dollars from " + transfer_donor + " to " + transfer_recip + ".")
        print(accounts)
        end()

#Create new account
def create_account():
	account_name = input("What is the first name on the account: ")
	account_amount = int(input("What amount would you like to deposit: "))
	accounts[account_name] = account_amount
	print()
	print("Account created under " + account_name + ". Returning you to the menu.")
	end()

#End menu
def end():
	print("Would you like to return to the menu? \n1. Yes \n2. No")
	answer = int(input("> "))
	if answer == 1:
		print("\033[H\033[J")
		menu()
	elif answer == 2:
		w = csv.writer(open("accounts.csv", "w"))
		for key, val in accounts.items():
			w.writerow([key, val])
		print("Thank you for choosing CS109 Credit Union and have a good day!")
	    

# Bank Accounts, check if csv file exists
if os.path.isfile('accounts.csv') is True:
	reader = csv.reader(open('accounts.csv', 'r'))
	accounts = {}
	for row in reader:
		k, v = row
		accounts[k] = v
if os.path.isfile('accounts.csv') is False:
	accounts={"Tucker": 6000, "Noah": 2500, "Eddie": 80000}

# # Actually running the program
# print("Welcome to CS109 Credit Union!")
# print("Where the security isn't present!")
# menu()

# window = Tk()
# window.title("CS109 Credit Union")
# #Creates label
# lbl = Label(window, text="Welcome to CS109 Credit Union", font=("Arial Bold", 10))
# #Positions label
# lbl.grid(column=0, row=0)
# #Sets window size
# window.geometry('350x200')
# #Creates button
# depositBtn = Button(window, text="Deposit")
# #Positions button
# depositBtn.grid(column=1, row=0)
# #Creates box for user input
# amount = Entry(window,width=15)
# #Positions entry box
# amount.grid(column=2, row=0)
 
# window.mainloop()

def chooseUser():
    return deposit("Noah")

btnNoah = Button(text="Noah", command=chooseUser)
btnNoah.pack()

mainloop()
