# Assignment: Due Amount
# Write a program to calculate the customer due amount after paying a bill of a certain amount

def calculate_due(total, paid):
    # Function to calculate due amount
    return total - paid

try:
    total_bill = float(input("Enter the total bill amount: "))
    amount_paid = float(input("Enter the amount paid: "))
    
    due = calculate_due(total_bill, amount_paid)
    
    if due > 0:
        print(f"Remaining due amount: {due:.2f}")
    elif due == 0:
        print("No due amount. Bill fully paid!")
    else:
        print(f"Change to return: {abs(due):.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values.")
