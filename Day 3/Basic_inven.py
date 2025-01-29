import json

FILENAME = "inventory.json"

class Item:
    def __init__(self, name, quantity, price):
        self.name = name.title()
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        return {"name": self.name, "quantity": self.quantity, "price": self.price}

class Inventory:
    def __init__(self):
        self.items = self.load_inventory()

    def load_inventory(self):
        try:
            with open(FILENAME, "r") as file:
                return [Item(**item) for item in json.load(file)]
        except FileNotFoundError:
            return []

    def save_inventory(self):
        with open(FILENAME, "w") as file:
            json.dump([item.to_dict() for item in self.items], file, indent=4)

    def add_item(self):
        name = input("Enter item name: ").strip().title()
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit: "))
            for item in self.items:
                if item.name == name:
                    item.quantity += quantity
                    break
            else:
                self.items.append(Item(name, quantity, price))
            print(f"Added {quantity} {name}(s) at ${price:.2f} each.")
        except ValueError:
            print("Invalid input! Enter numbers for quantity and price.")

    def view_inventory(self):
        if not self.items:
            print("No items in inventory.")
            return
        total_value = sum(item.quantity * item.price for item in self.items)
        for item in self.items:
            print(f"{item.name}: {item.quantity} units | ${item.price:.2f} each | Total: ${item.quantity * item.price:.2f}")
            if item.quantity < 5:
                print(f"Low stock alert: Only {item.quantity} left!")
        print(f"Total Inventory Value: ${total_value:.2f}")

    def update_stock(self):
        name = input("Enter item sold: ").strip().title()
        for item in self.items:
            if item.name == name:
                try:
                    sold = int(input(f"Enter quantity sold (Available: {item.quantity}): "))
                    if 0 < sold <= item.quantity:
                        item.quantity -= sold
                        print(f"Sold {sold} {name}(s). Remaining: {item.quantity}")
                        if item.quantity < 5:
                            print(f"Low stock alert: Only {item.quantity} left!")
                    else:
                        print("Invalid quantity!")
                except ValueError:
                    print("Enter a valid number!")
                return
        print("Item not found!")

    def run(self):
        while True:
            print("\n1. Add Item\n2. View Inventory\n3. Update Stock\n4. Save & Exit")
            choice = input("Choose an option (1-4): ")
            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.view_inventory()
            elif choice == "3":
                self.update_stock()
            elif choice == "4":
                self.save_inventory()
                print("Inventory saved. Goodbye!")
                break
            else:
                print("Invalid choice! Enter a number 1-4.")

if __name__ == "__main__":
    Inventory().run()
