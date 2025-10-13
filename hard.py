# hard (midterms exam)

print("Monthly Loan Payment Table")
loan = eval(input("Enter loan amount: "))
loan_period = eval(input("Enter loan period in years: "))

months = loan_period * 12
principal = loan / months
balance = loan
print("|\tMonths\t|\tPrincipal Payment\t|\tRemaining Balance\t|\tInterest\t|")

for j in range (1, months + 1, 1):
    balance -= principal
    interest = balance * 0.03
    monthly = principal + interest
    print(f"|\t{j}\t\t|\t{round(principal, 2)}\t\t|\t{round(balance, 2)}\t\t|\t{round(interest, 2)}\t\t|\t{round(monthly, 2)}\t\t|")