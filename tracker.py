print("========================================")
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("========================================")

name = input("What's your name?: ")
tax_rate = float(input("Tax rate %?: "))
budget = float(input("Your budget?: $"))

print(f"Welcome, {name}!")
print("")
print("MAIN MENU")
print("  [1] Add an expense")
print("  [2] View all expenses (coming soon)")
print("  [3] Show total spent")
print("  [4] Exit")
print("")

subtotal = 0
expenses = 0

while True:
    
    choice = input("Choice 1-4: ")

    if choice == "1":

        amount = float(input("Amount: "))

        subtotal+= amount
        expenses += 1

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense")
        else:
            print("  Small expense")

    elif choice == "2":
            
            print("  Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":

        tax = subtotal * (tax_rate / 100)
        grand_total = subtotal + tax

        print(f"  Expenses: \t{expenses}")
        print(f"  Subtotal: \t${subtotal:.1f}")
        print(f"  Tax ({tax_rate:.1f}): \t${tax:.1f}")
        print(f"  Grand total: \t${grand_total:.1f}")

        if grand_total > budget:
            print(f"  Over budget by ${grand_total - budget:.2f}!")
        elif grand_total > budget * 0.90:
            print(f"  Careful! only ${budget - grand_total:.2f} left.")
        else:
            print(f"  Within budget. ${budget - grand_total:.2f} left.")

    elif choice == "4":

        print(f"Goodbye, {name}!")
        break
    else:

        print("  Please choose 1, 2, 3 or 4.")


print("----------------------------------------")
print("Made by: Frenz Louis C. Bautista | Installment 5")
print("========================================")