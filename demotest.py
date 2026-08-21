# ==========================================
# DATA STRUCTURES SETUP
# ==========================================
# 1. TUPLE: Fixed Identity Data
# (Customer_ID, Date_Opened, Account_Type)
# ==========================================
account_dtl=(14948,'2026-08-21','Saving')
#=========================================
# 2. List:Sequential Transactional History
#( (Positive numbers = deposits, Negative = withdrawals))
#=========================================
transaction_hitory=[100,-45,900,-500]
#=======================================
# 3. Dictionary: Complete Profile 
# (Combines everything together)
#======================================
bank_customer = {'name':'venkat',
               "email": "venkat@email.com",
               'is_active':True,
               'identity':account_dtl,
               'transactions':transaction_hitory}
print('customer Name:',bank_customer['name'])
print('customer_id:',bank_customer['identity'][0])
print('account_type:',bank_customer['identity'][2])
bank_customer['transactions'].append(555)
print('after new transaction',bank_customer['transactions'])
total_balance=sum(bank_customer['transactions'])
print(f"current balance: ${total_balance}")
# ==========================================
# BALANCE CALCULATION & CONDITIONAL ALERT
# ==========================================
bank_customer['transactions'].append(-1020)
current_balance=sum(bank_customer['transactions'])
if current_balance < 0:
    print(f"Dear {bank_customer['name']}, Account is over drawn!",'balance:',current_balance)
else:
    print("Account status: Healthy.")
#------Every Transaction Processing using for loop----------
running_balance=0.0
bank_customer['transactions'].append(1500)
for transaction in transaction_hitory:
    if transaction>0:
        print(f"Deposited : ${transaction}")
    else:
        print(f"Withdraw: ${transaction}")
    running_balance += transaction
    print(f"final settlement balance ${running_balance}")
current_balance=sum(bank_customer['transactions'])
print(current_balance)
#----Draining Funds Until a while Condition Met ------
subscription_amt=299.50
month_paid_status=0
while current_balance>0:
    current_balance -=subscription_amt
    month_paid_status+=1
    print(f"this month subdcription amount {subscription_amt} deducted and current balance {current_balance}")
print(f"Insufficient funds")