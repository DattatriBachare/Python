import time

print ('Please insesrt Your CARD : ')

time.sleep(10)

password = 7394

pin = int(input("Enter your PIN : "))

Balance = 5000
if pin == password:
    while True:

        print("""
          1 == Balance Enquiry
          2 == Withdraw Balance
          3 == deposit Balance
          4 == Exit
          """)
        try:
            option = int(input("Please enter your choice : "))
        except:
            print("Please Enter Valid Input : ")

        if option == 1:
            print(f"Your Current Balance : {Balance}")

            print("----------------------------------------------------------")
            print("----------------------------------------------------------")

        if option == 2:
            withdraw_Amount = int(input("Please Enter Amount to Withdraw : "))

            print("----------------------------------------------------------")
            print("----------------------------------------------------------")

            Balance = Balance - withdraw_Amount


            print(f"{withdraw_Amount} Debited from your Account : ")

            print("----------------------------------------------------------")
            print("----------------------------------------------------------")

            print(f" Available balance : {Balance}")

            print("----------------------------------------------------------")
            print("----------------------------------------------------------")
    
        if option == 3:
            deposite_amount = int(input("Enter amount to Deposit : "))

            print("----------------------------------------------------------")
            print("----------------------------------------------------------")

            Balance = Balance + deposite_amount

            print(f"{deposite_amount} Credited to your Account : ")

            print("----------------------------------------------------------")
            print("----------------------------------------------------------")

            print(f"Your Current Balance : {Balance}")

            print("----------------------------------------------------------")
            print("----------------------------------------------------------")
    
        if option == 4:
        
            break
else:
    print(""" You Entered Wrong Password XXXX
           Please Try Again :->  """)