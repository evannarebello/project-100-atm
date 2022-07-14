class Atm(object):
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin

    def balance_enquiry(self):
        print("Your balance is 10000")

    def cash_withdrawl(self,amount):
        new_amount = 10000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))

def main():
    cardnumber=input("enter your card number:")
    pinnumber=input("enter your pin number:")

    newuser = Atm(cardnumber,pinnumber)
    print("choose your activity ")
    print("1.balance enquiry   2.withdrawl")
    activity=int(input("enter activity number:"))
    if activity==1:
        newuser.balance_enquiry()
    elif activity==2:
        amount=int(input("enter the amount you want to withdraw:"))
        newuser.cash_withdrawl(amount)
    else:
        print("enter a valid number:")

main()

