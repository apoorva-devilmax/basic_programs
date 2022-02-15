import sys

acc_balance = 10000
option = int(sys.argv[1])
if option == 1:
    # check balance
    print('Your account balance is $', acc_balance)
elif option == 2:
    # withdraw
    amount = float(input('How much do you want to withdrawl? '))
    if amount <= 0:
        print('Please enter amount greater than zero.')
    else:
        print('You have successfully withdrawl $', amount, 'amount. Your updated balance is', (acc_balance - amount))
elif option == 3:
    # deposit cash
    amount = float(input('How much do you want to deposit in cash? '))
    if amount <= 0:
        print('Please enter amount greater than zero.')
    else:
        print('You have successfully deposited $', amount, 'amount. Your updated balance is', (acc_balance + amount))
elif option == 4:
    # deposit check
    amount = float(input('How much do you want to deposit in check? '))
    if amount <= 0:
        print('Please enter amount greater than zero.')
    else:
        print('You have successfully deposited $', amount, 'amount. Your updated balance is', (acc_balance + amount))
else:
    print('Wrong choice passed!')