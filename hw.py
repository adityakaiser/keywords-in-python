total_bill = float(input("Enter the total bill amount: "))
amount_paid = float(input("Enter the amount paid by the customer: "))

due_amount = total_bill - amount_paid

print(f"The remaining due amount is: {due_amount}")