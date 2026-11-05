#import
import time
from datetime import datetime
balance=100
VALID_PIN=str(4928) 
#pin valid function
def valid_pin(valid_pin):
    attempts = 3

    while attempts > 0:
        pin = input("Enter your Pin: ")
        if pin == valid_pin:
            return True
        else:
            attempts -= 1
            print("Invalid Pin")

    print("Too many tries, account has been frozen")
    return False
#withdraw function
def withdraw_valid(balance, withdraw_amount):
    if withdraw_amount > balance:
        return False
    else:
        return True
#Balance update function
def update_balance(balance, withdraw_amount):
    return balance - withdraw_amount
#display first menu
while True or withdraw == "No" :
    print("""<<<ATM MACHINE>>>
Do you want to withdraw money?""")
    withdraw=input("(Yes/No)").capitalize()
    withdrawValid = False
    #pin validation

    
    if withdraw == "Yes" and valid_pin(VALID_PIN):
        print("Pin valid")
        print(f"<<<You have £{balance} in your account>>>")
        while withdrawValid == False :
            withdrawAmount=input("""<<<Select your withdraw amount:>>>
1.£10
2.£20
3.£50
4.£100
5.Custom
Enter:""")
            if withdrawAmount == "1":
                withdrawAmount = 10
                withdrawValid=True
            elif withdrawAmount == "2":
                withdrawAmount = 20
                withdrawValid=True
            elif withdrawAmount == "3":
                withdrawAmount = 50
                withdrawValid=True
            elif withdrawAmount == "4":
                withdrawAmount = 100
                withdrawValid=True
            elif withdrawAmount == "5":
                withdrawAmount=1
                while withdrawAmount %5 != 0:
                    withdrawAmount= int(input("How much do you want to withdraw?"))
                    if withdrawAmount %5 != 0:
                        print("Cannot withdraw this amount as it has to be a factor of 5(£5 notes)")
                withdrawValid=True
            else:
                print("That is not a valid number ")
        
    
    elif withdraw == "No":
        withdrawAmount="noWithdraw"
    elif withdraw not in ["Yes","No"]:
        withdrawAmount="InvalidInput"
    else:
        withdrawAmount="IncorrectPin"
    
    sufficientFunds=True
    withdraw=True
    if withdrawAmount=="noWithdraw":
        print("You have chosen to not withdraw")
        balance=100
        withdraw=False
        time.sleep(1)
    elif withdrawAmount=="IncorrectPin":
        print("You have entered an incorrect pin too many times")
        withdraw=False
        time.sleep(1)
    elif withdrawAmount=="InvalidInput":
        print("Your input is invalid")
        withdraw=False
        time.sleep(1)

    else:
        if withdraw_valid(balance,withdrawAmount):
            balance = update_balance(balance,withdrawAmount)
        else:
            print("<<<Insufficient Funds>>>")
            sufficientFunds=False
            time.sleep(4)


#display receipt
    if sufficientFunds==True and withdraw:
        LINE_DELAY = 0.5
        print("----------Receipt----------")
        time.sleep(LINE_DELAY)
        print(datetime.now())
        time.sleep(LINE_DELAY)
        print(f"balance before: {balance + withdrawAmount}")
        time.sleep(LINE_DELAY)
        print(f"withdraw amount: -{withdrawAmount}")
        time.sleep(LINE_DELAY)
        print(f"current balance: {balance}")
        time.sleep(LINE_DELAY)
        print("Thank you for your transaction!")
        time.sleep(4)

time.sleep(1)
print("Thank you for using me")
