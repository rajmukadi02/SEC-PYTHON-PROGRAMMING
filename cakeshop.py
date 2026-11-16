cakes = {
    1: {"name": "Chocolate Cake", "price": 500},
    2: {"name": "Vanilla Cake", "price": 400},
    3: {"name": "Black Forest Cake", "price": 600},
    4: {"name": "Red Velvet Cake", "price": 700},
    5: {"name": "Pineapple Cake", "price": 450},
    6: {"name": "Dutch Truffel", "price": 750},
    7: {"name": "Chocolava Cake", "price": 100}
}

while True:

    print("\n===================================")
    print("            WELCOME ")
    print("               TO ")
    print("       MR.RAJ CAKE SHOP")
    print("===================================")

    print("\n========== MAIN MENU ==========")
    print("1. View Cake Menu")
    print("2. Add New Cake")
    print("3. Search Cake")
    print("4. Update Cake Details")
    print("5. Delete Cake")
    print("6. Generate Customer Bill")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        print("\n========== CAKE MENU ==========")
        print("-----------------------------------")

        for cake_id, details in cakes.items():

            print("Cake ID:", cake_id)
            print("Cake Name:", details["name"])
            print("Price: Rs.", details["price"])
            print("-----------------------------------")

    elif choice == "2":

        print("\n========== ADD NEW CAKE ==========")

        cake_id = max(cakes.keys(), default=0) + 1

        name = input("Enter Cake Name: ").strip()

        try:
            price = int(input("Enter Cake Price: "))

            if name == "" or price <= 0:
                print("Please enter a valid name and price!")

            else:
                cakes[cake_id] = {
                    "name": name,
                    "price": price
                }

                print("\nCake Added Successfully!")
                print("Cake ID:", cake_id)

        except ValueError:
            print("Please enter a valid price!")

    elif choice == "3":

        print("\n========== SEARCH CAKE ==========")

        search_name = input("Enter Cake Name: ").strip()

        found = False

        for cake_id, details in cakes.items():

            if details["name"].lower() == search_name.lower():

                print("\nCake Found!")
                print("Cake ID:", cake_id)
                print("Cake Name:", details["name"])
                print("Price: Rs.", details["price"])

                found = True
                break

        if not found:
            print("Cake Not Found!")

    elif choice == "4":

        print("\n========== UPDATE CAKE ==========")

        try:
            cake_id = int(input("Enter Cake ID: "))

            if cake_id in cakes:

                print("Current Name:", cakes[cake_id]["name"])
                print("Current Price:", cakes[cake_id]["price"])

                new_name = input("Enter New Cake Name: ").strip()
                new_price = int(input("Enter New Price: "))

                if new_name != "" and new_price > 0:

                    cakes[cake_id]["name"] = new_name
                    cakes[cake_id]["price"] = new_price

                    print("Cake Details Updated Successfully!")

                else:
                    print("Invalid Name or Price!")

            else:
                print("Cake ID Not Found!")

        except ValueError:
            print("Please enter valid details!")

    elif choice == "5":

        print("\n========== DELETE CAKE ==========")

        try:
            cake_id = int(input("Enter Cake ID: "))

            if cake_id in cakes:

                print("Cake Name:", cakes[cake_id]["name"])

                confirm = input("Are you sure? (yes/no): ")

                if confirm.lower() == "yes":

                    del cakes[cake_id]

                    print("Cake Deleted Successfully!")

                else:
                    print("Delete Cancelled!")

            else:
                print("Cake ID Not Found!")

        except ValueError:
            print("Please enter a valid Cake ID!")

    elif choice == "6":

        print("\n========== GENERATE CUSTOMER BILL ==========")

        customer = input("Enter Customer Name: ").strip()

        bill = 0
        purchased_cakes = []

        while True:

            try:
                cake_id = int(input("\nEnter Cake ID (0 to finish): "))

                if cake_id == 0:
                    break

                if cake_id in cakes:

                    quantity = int(input("Enter Quantity: "))

                    if quantity <= 0:
                        print("Invalid Quantity!")
                        continue

                    cake_name = cakes[cake_id]["name"]
                    price = cakes[cake_id]["price"]

                    amount = price * quantity
                    bill = bill + amount

                    purchased_cakes.append({
                        "name": cake_name,
                        "price": price,
                        "quantity": quantity,
                        "amount": amount
                    })

                    print("Cake Added To Bill!")

                else:
                    print("Invalid Cake ID!")

            except ValueError:
                print("Please enter valid numbers!")

        print("\n====================================================")
        print("                  CUSTOMER BILL")
        print("====================================================")

        print("Customer Name:", customer)
        print("----------------------------------------------------")

        print("{:<20} {:<10} {:<8} {:<10}".format(
            "Cake Name", "Price", "Qty", "Amount"))

        print("----------------------------------------------------")

        for item in purchased_cakes:

            print("{:<20} Rs.{:<7} {:<8} Rs.{:<10}".format(
                item["name"],
                item["price"],
                item["quantity"],
                item["amount"]
            ))

        print("----------------------------------------------------")

        print("TOTAL AMOUNT: Rs.", bill)

        print("====================================================")
        print("             THANK YOU! VISIT AGAIN!")
        print("====================================================")

    elif choice == "7":

        print("\nThank You for Visiting Cake Shop!")
        print("Application Closed.")
        break

    else:

        print("\nInvalid Choice! Please Try Again.")



convert the above code into c programing
