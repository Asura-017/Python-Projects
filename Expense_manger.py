def expense_tracker():
    # Dictionary to store expenses
    expenses = {}

    print("Welcome to the Enhanced Expense Tracker!")

    while True:
        # Display the menu
        print("\nWhat would you like to do?")
        print("1. Add a new expense")
        print("2. Show all expenses")
        print("3. Update an expense")
        print("4. Delete an expense")
        print("5. Calculate total expenses")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            # Add a new expense
            category = input("Enter the category (e.g., Food, Transport): ").strip()
            amount = input("Enter the amount: ")

            if amount.isdigit():
                amount = float(amount)
                if category in expenses:
                    expenses[category] += amount
                else:
                    expenses[category] = amount
                print(f"Added ${amount:.2f} to {category}.")
            else:
                print("Invalid amount. Please enter a number.")

        elif choice == '2':
            # Show all expenses
            print("\nHere are your expenses:")
            if expenses:
                for category, amount in expenses.items():
                    print(f"- {category}: ${amount:.2f}")
            else:
                print("No expenses recorded yet.")

        elif choice == '3':
            # Update an expense
            category = input("Enter the category you want to update: ").strip()
            if category in expenses:
                new_amount = input(f"Enter the new amount for {category}: ")
                if new_amount.isdigit():
                    expenses[category] = float(new_amount)
                    print(f"Updated {category} to ${float(new_amount):.2f}.")
                else:
                    print("Invalid amount. Please enter a number.")
            else:
                print(f"No expense found for the category '{category}'.")

        elif choice == '4':
            # Delete an expense
            category = input("Enter the category you want to delete: ").strip()
            if category in expenses:
                del expenses[category]
                print(f"Deleted the expense for {category}.")
            else:
                print(f"No expense found for the category '{category}'.")

        elif choice == '5':
            # Calculate total expenses
            total = sum(expenses.values())
            print(f"\nYour total expenses are: ${total:.2f}")

        elif choice == '6':
            # Exit the program
            print("Thank you for using the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Start the Expense Tracker
expense_tracker()
