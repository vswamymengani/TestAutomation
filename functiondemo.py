"""Topic: Functions"""
#Simple Function, No parameters and No returns
def welcome_banner():
    print("--------------------------")
    print("  Welcome to Apex Banking  ")
    print("--------------------------")
###Parameterized Function (With Inputs, No Return)
###Greets a specific customer using their profile details
def customer_greeting(customer_name,Account_type):
    print(f"Hello,{customer_name}! managing your {Account_type} Account")
welcome_banner()
customer_greeting("Venkat","Saving")
print("                           ")
##Function with a Return Value (With Inputs and Output)
##Calculates total balance from a list of transactions
def bank_transactions(transactions):
    total=sum(transactions)
    return total
my_transactions=[120,800,-100,-99,500]
current_balance=bank_transactions(my_transactions)
print(f"my current balance is:  ${current_balance}")
print("                           ")
print("--------------------------")