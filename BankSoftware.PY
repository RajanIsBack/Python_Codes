'''ATM Simulation
Check Balance   Make a Withdrawal   Pay In   Return Card
'''

bank_pin =5267
entered_pin = int(input("Enter your bank pin"))
if(entered_pin != bank_pin):
    print("Wrong pin.Exiting and returning card")
else:
    print("WELCOME USER !!. Choose from below options")
    print("1.Check Balance")
    print("2.Withdraw Money")
    print("3.Cash Credit")
    print("4.Return Card")
    print("5.Change Password")
    user_option=int(input("Enter an option number"))
    if(user_option==1):
        print("Balance is 55,283.00")
    elif(user_option==2):
        withdrawn_amount=int(input("Enter the amount to be withdrawn"))
    elif(user_option==3):
        pay_in_amount=int(input("Enter the amount of money you want to Pay In"))
        print("Press OK to confirm")
    elif(user_option==4):
        print("Press CANCEL to return your Card")
    elif (user_option == 5):
        input1=int(input("Please enter your new 6 digit password"))
        input2=int(input("Please enter your new 6 digit password one again to confirm"))
        if (input1==input2):
            print("PASSWORD CHANGED SUCCESSFULLY !!")
    else:
        print("Invalid Input")


    print("Thanks for Banking with EDUREKA BANK. Visit Again!!")








