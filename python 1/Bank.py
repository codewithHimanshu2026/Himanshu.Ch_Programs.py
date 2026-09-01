bal=1000000
withdrawal=True

while withdrawal:
    amount=int(input("Enter amount to withdrawal"))
    if(amount<=bal):
        print("Amount debited")
        bal=bal-amount
        print("Your current bal",bal)
    else:
        print("Insufficient bal")

    choice=input("Do you need to withdraw again:(yes/no)")
    if choice.lower()=="no":
        withdrawal=False
        