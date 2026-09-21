class Farmer:
    def __init__(self, farmer_id, name, crop, quantity):
        self.farmer_id = farmer_id
        self.name = name
        self.crop = crop
        self.quantity = quantity

    def display(self):
        print("\nFarmer ID:", self.farmer_id)
        print("Name:", self.name)
        print("Crop:", self.crop)
        print("Quantity:", self.quantity, "kg")


farmers = []
market_prices = {
    "Rice": 45,
    "Wheat": 35,
    "Maize": 30,
    "Tomato": 25,
    "Potato": 20
}

while True:
    print("\n===== AGRICONNECT =====")
    print("1. Register Farmer")
    print("2. View Farmers")
    print("3. Search Farmer")
    print("4. View Market Prices")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        farmer_id = input("Enter Farmer ID: ")
        name = input("Enter Farmer Name: ")
        crop = input("Enter Crop Name: ")
        quantity = int(input("Enter Quantity (kg): "))

        farmer = Farmer(farmer_id, name, crop, quantity)
        farmers.append(farmer)

        print("Farmer registered successfully!")

    elif choice == "2":
        if len(farmers) == 0:
            print("No farmer records found.")
        else:
            for farmer in farmers:
                farmer.display()

    elif choice == "3":
        search_id = input("Enter Farmer ID: ")
        found = False

        for farmer in farmers:
            if farmer.farmer_id == search_id:
                farmer.display()
                found = True
                break

        if not found:
            print("Farmer not found!")

    elif choice == "4":
        print("\nCurrent Market Prices")
        for crop, price in market_prices.items():
            print(f"{crop}: ₹{price}/kg")

    elif choice == "5":
        print("Thank you for using AgriConnect!")
        break

    else:
        print("Invalid choice! Try again.")