data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(transactions):
  for amount, statement in transactions:
    print(f"${amount} - {statement}")


def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposited = sum(deposits)
  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0 ]
  total_withdrawn = sum(withdrawals)
  balance = sum(deposits) + sum(withdrawals)
  print(f"Total Deposited: {total_deposited}")
  print(f"Total Withdrawn: {total_withdrawn}")
  print(f"Balance: {balance}")

def analyze_transactions(transactions):
  transactions.sort()
  largest_withdrawal = transactions[0]
  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0 ]
  total_withdrawals = sum(withdrawals)
  average_withdrawal = total_withdrawals / len(withdrawals) if len(withdrawals) > 0 else 0
  largest_deposit = transactions[-1]
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposit = sum(deposits)
  average_deposit = total_deposit / len(deposits) if len(deposits) > 0 else 0
  print(f"Largest Withdrawal: {largest_withdrawal}")
  print(f"Average Withdrawal: {average_withdrawal}")
  print(f"Largest Deposit: {largest_deposit}")
  print(f"Average deposit: {average_deposit}")


while True:
  choice =  input("What option would you like? ")
  if choice == "print":
    print_summary(data)
  elif choice == "analyze":
    analyze_transactions(data)
  elif choice == "stop":
    break
  else:
    print("Invalid choice")