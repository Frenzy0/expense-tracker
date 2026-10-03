# Author: Frenz Louis C. Bautista
print("========================================")
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("========================================")
print("")
print("Welcome! This is your personal expense tracker.")
print("")
print("MAIN MENU")
print("  [1] Add an expense \t\t\t(coming soon)")
print("  [2] View all expenses \t\t(coming soon)")
print("  [3] Show total spent \t\t\t(coming soon)")
print("  [4] Exit \t\t\t\t(coming soon)")
print("")
name = input("What's your name?: ")
print(f"Welcome, {name}!" + " Let's log two expenses.")
print("")
item1 = input("First expenses: ") 
amount1 = float(input("Amount: "))
item2 = input("First expenses: ") 
amount2 = float(input("Amount: "))
tax_rate = float(input("Tax rate %?: "))
budget = float(input("Your budget?: $"))

subtotal = amount1 + amount2
average = subtotal / 2
tax = subtotal * (tax_rate / 100)
grand_total = subtotal + tax

over_budget = grand_total > budget
left_in_budget = budget - grand_total


print("")
print("----------------------------------------")
print("SUMMARY")
print(f" - {item1}: \t${amount1}")
print(f" - {item2}: \t${amount2}")
total = amount1 + amount2
print(f"Total spent: \t${total}")
average = (amount1 + amount2) / 2
print(f"Average: \t${average}")
print(f"Subtotal:    \t${subtotal:.1f}")
print(f"Average:     \t${average:.2f}")
print(f"Tax ({tax_rate:.1f}%): \t${tax:.1f}")
print(f"Grand total: \t${grand_total:.1f}")
print(f"Over budget?: \t{over_budget}")
print(f"Left in budget: ${left_in_budget:.1f}")
print("----------------------------------------")
print("Made by: Frenz Louis C. Bautista | Installment 3")
print("========================================")