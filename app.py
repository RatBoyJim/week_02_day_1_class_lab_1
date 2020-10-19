from modules.bank_account import *
import pdb 

# account = {
#     "holder_name": "Colin",
#     "balance": 100,
#     "type": "business"
# }

bank_account = BankAccount("Colin", 100, "business")
bank_account_2 = BankAccount("Michael", 50, "personal")
bank_account_3 = BankAccount("Yer Maw", 25, "savings")
# pdb.set_trace()

print("Holder name: " + bank_account.holder_name)

bank_account.holder_name = "Roosa"

print("Holder name after: " + bank_account.holder_name)
print(bank_account.holder_name, bank_account_2.holder_name)

bank_account.pay_in(20)

print(bank_account.balance)

# make pay_monthly_fee method for BankAccount which will decrease 
# the amount of money in the account by 50 

# Modify pay_monthly_fee to only 
# deduct 50 for business accounts. Deduct 10 for any other account type

print(bank_account.holder_name + "'s Account balance is £" + str(bank_account.balance))
bank_account.pay_monthly_fee()
print(bank_account.holder_name + "'s Account balance is £" + str(bank_account.balance))

print(bank_account_2.holder_name + "'s Account balance is £" + str(bank_account_2.balance))
bank_account_2.pay_monthly_fee()
print(bank_account_2.holder_name + "'s Account balance is £" + str(bank_account_2.balance))

print(bank_account_3.holder_name + "'s Account balance is £" + str(bank_account_3.balance))
bank_account_3.pay_monthly_fee()
print(bank_account_3.holder_name + "'s Account balance is £" + str(bank_account_3.balance))