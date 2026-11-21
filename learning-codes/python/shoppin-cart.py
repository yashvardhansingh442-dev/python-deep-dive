#This is another example code where we will take input from the user and trying to show we are so cool.



TAX_RATE = 0.10

cart = []


def add_item():
    name = input("Enter item name: ").strip()

    if not name:
        print("Item name cannot be empty.")
        return

    try:
        price = float(input("Enter price: $"))
        quantity = int(input("Enter quantity: "))

        if price <= 0 or quantity <= 0:
            print("Price and quantity must be positive.")
            return

    except ValueError:
        print("Invalid input. Try again.")
        return

    cart.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

    print(f"{name} added to cart.")


def view_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\nYour Cart")
    print("-" * 40)

    for i, item in enumerate(cart, start=1):
        item_total = item["price"] * item["quantity"]

        print(
            f"{i}. {item['name']} | "
            f"{item['quantity']} x ${item['price']:.2f} "
            f"= ${item_total:.2f}"
        )

    print("-" * 40)
    print(f"Subtotal: ${calculate_subtotal():.2f}")


def calculate_subtotal():
    return sum(
        item["price"] * item["quantity"]
        for item in cart
    )


def remove_item():
    view_cart()

    if not cart:
        return

    try:
        choice = int(input("Enter item number to remove: "))

        if 1 <= choice <= len(cart):
            removed = cart.pop(choice - 1)
            print(f"{removed['name']} removed.")
        else:
            print("Invalid item number.")

    except ValueError:
        print("Please enter a valid number.")


def update_quantity():
    view_cart()

    if not cart:
        return

    try:
        choice = int(input("Enter item number: "))

        if not 1 <= choice <= len(cart):
            print("Invalid item number.")
            return

        quantity = int(input("Enter new quantity: "))

        if quantity <= 0:
            print("Quantity must be positive.")
            return

        cart[choice - 1]["quantity"] = quantity
        print("Quantity updated.")

    except ValueError:
        print("Please enter a valid number.")


def checkout():
    if not cart:
        print("Your cart is empty.")
        return

    view_cart()

    subtotal = calculate_subtotal()
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    print("\nReceipt")
    print("-" * 30)
    print(f"Subtotal:  ${subtotal:.2f}")
    print(f"Tax (10%): +${tax:.2f}")
    print("-" * 30)
    print(f"Total:     ${total:.2f}")
    print("\nThank you for shopping!")


def main():
    while True:
        print("\nShopping Cart")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Update quantity")
        print("5. Checkout")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            update_quantity()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
