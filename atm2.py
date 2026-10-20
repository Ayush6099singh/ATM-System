Balance=5000.00
pin = 7970
tranctions=[]
attempts = 0

while attempts < 3:
    user_pin = int(input("enter your pin"))
    if user_pin == pin:
        print("login successfully")
        break
    else:
        attempts+=1
        print("incorrect pin")

if attempts == 3:
    print("your account block temporarly")

else:
    while True:
        print("\n====ATM MENU====")
        print("1.cherck balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")
        choice = input("Enter your choice  ")

        if choice == '1':
            print("your balance is: ",Balance)
        elif choice == '2':
            amount = float(input("enter your amount:"))
            if amount <= Balance:
                amount+=Balance
                print("the deposit is",amount)
            else:
                print("insufficient balance")
        elif choice == '3': 
            amount = float(input("enter your amount:")) 
            if amount <= Balance:
                    Balance -= amount
                    print("the withdraw is",amount)     
            else:
                print("insufficient balance")
        elif choice == '4':
            print("thank you for using ATM")
            break   

    else:
        print("invalid choice")