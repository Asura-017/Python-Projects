def expense_tracker():
    # Dictionary to store expenses
    expenses = {}

    print("Welcome to the Expense Tracker!")

    while True:
        # Display the menu
        print("\nWhat would you like to do?")
        print("1. Add a new expense")
        print("2. Show all expenses")
        print("3. Calculate total expenses")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Add a new expense
            category = input("Enter the category (e.g., Food, Transport): ").strip()
            amount = input("Enter the amount: ")

            # Check if the amount is valid
            if amount.isdigit():
                amount = float(amount)  # Convert to a number
                if category in expenses:
                    expenses[category] += amount
                else:
                    expenses[category] = amount
                print(f"Added ${amount:.2f} to {category}.")
            else:
                print("Please enter a valid number for the amount.")

        elif choice == '2':
            # Show all expenses
            print("\nHere are your expenses:")
            if expenses:
                for category, amount in expenses.items():
                    print(f"- {category}: ${amount:.2f}")
            else:
                print("No expenses recorded yet.")

        elif choice == '3':
            # Calculate and display total expenses
            total = sum(expenses.values())
            print(f"\nYour total expenses are: ${total:.2f}")

        elif choice == '4':
            # Exit the program
            print("Thank you for using the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Start the Expense Tracker
expense_tracker()

