

# BUS PASS MANAGEMENT SYSTEM

import json
import os

pass_types = {
    "Monthly": 500,
    "Quarterly": 1350,
    "Yearly": 4800
}

file_name = "buspass.txt"


def load_passes():

    if os.path.exists(file_name):

        file = open(file_name, "r")
        data = file.read()
        file.close()

        if data == "":
            return []

        return json.loads(data)

    else:
        return []


def save_passes(passes):

    file = open(file_name, "w")
    json.dump(passes, file, indent=4)
    file.close()


def generate_id(passes):

    number = 100

    for customer in passes:
        old_id = customer["id"]
        old_number = int(old_id[2:])

        if old_number > number:
            number = old_number

    return "BP" + str(number + 1)


def calculate_fee(pass_type, category):

    fee = pass_types[pass_type]

    if category == "Student":
        fee = fee - (fee * 25 / 100)

    return fee


def find_customer(passes, pass_id):

    for customer in passes:

        if customer["id"] == pass_id.upper():
            return customer

    return None


def show_details(customer):

    print("\n----------------------------")
    print("Pass ID  :", customer["id"])
    print("Name     :", customer["name"])
    print("Route    :", customer["route"])
    print("Pass Type:", customer["type"])
    print("Category :", customer["category"])
    print("Fee      : Rs.", customer["fee"])
    print("Validity :", customer["validity"], "days")
    print("----------------------------")


def issue_pass(passes):

    print("\n--- ISSUE NEW PASS ---")

    name = input("Enter customer name: ").strip()
    route = input("Enter bus route: ").strip()

    if name == "" or route == "":
        print("Name and route cannot be empty!")
        return

    pass_type = input(
        "Enter pass type (Monthly/Quarterly/Yearly): "
    ).strip().title()

    if pass_type not in pass_types:
        print("Invalid pass type!")
        return

    category = input(
        "Enter category (General/Student): "
    ).strip().title()

    if category != "General" and category != "Student":
        print("Invalid category!")
        return

    fee = calculate_fee(pass_type, category)

    if pass_type == "Monthly":
        days = 30
    elif pass_type == "Quarterly":
        days = 90
    else:
        days = 365

    customer = {
        "id": generate_id(passes),
        "name": name,
        "route": route,
        "type": pass_type,
        "category": category,
        "fee": fee,
        "validity": days
    }

    passes.append(customer)
    save_passes(passes)

    print("\nPass issued successfully!")
    show_details(customer)


def renew_pass(passes):

    print("\n--- RENEW BUS PASS ---")

    pass_id = input("Enter pass ID: ").strip().upper()
    customer = find_customer(passes, pass_id)

    if customer == None:
        print("Customer not found!")
        return

    new_type = input(
        "Enter new pass type (Monthly/Quarterly/Yearly): "
    ).strip().title()

    if new_type not in pass_types:
        print("Invalid pass type!")
        return

    customer["type"] = new_type
    customer["fee"] = calculate_fee(
        new_type, customer["category"]
    )

    if new_type == "Monthly":
        customer["validity"] = 30
    elif new_type == "Quarterly":
        customer["validity"] = 90
    else:
        customer["validity"] = 365

    save_passes(passes)

    print("\nPass renewed successfully!")
    show_details(customer)

def search_pass(passes):

    print("\n--- SEARCH BUS PASS ---")

    pass_id = input("Enter pass ID: ").strip().upper()
    customer = find_customer(passes, pass_id)

    if customer == None:
        print("Pass not found!")
    else:
        show_details(customer)

def view_passes(passes):

    print("\n--- ALL REGISTERED CUSTOMERS ---")

    if len(passes) == 0:
        print("No passes issued yet.")
    else:

        for customer in passes:
            show_details(customer)

def edit_pass(passes):

    print("\n--- EDIT BUS PASS ---")

    pass_id = input("Enter pass ID: ").strip().upper()
    customer = find_customer(passes, pass_id)

    if customer == None:
        print("Customer not found!")
        return

    print("\nCurrent customer details:")
    show_details(customer)

    print("\nPress Enter to keep the old details.")

    name = input("New name: ").strip()
    route = input("New route: ").strip()

    new_category = input(
        "New category (General/Student): "
    ).strip().title()

    if new_category != "" and new_category not in ["General", "Student"]:
        print("Invalid category!")
        return

    if name != "":
        customer["name"] = name

    if route != "":
        customer["route"] = route

    if new_category != "":
        customer["category"] = new_category

    save_passes(passes)

    print("\nCustomer details updated successfully!")
    show_details(customer)

def delete_pass(passes):

    print("\n--- DELETE BUS PASS ---")

    pass_id = input("Enter pass ID: ").strip().upper()
    customer = find_customer(passes, pass_id)

    if customer == None:
        print("Customer not found!")
        return

    print("\nCustomer details:")
    show_details(customer)

    confirm = input(
        "Are you sure you want to delete this pass? (Yes/No): "
    ).strip().title()

    if confirm == "Yes":

        passes.remove(customer)
        save_passes(passes)

        print("Pass deleted successfully!")

    else:
        print("Deletion cancelled.")


def main():

    passes = load_passes()

    while True:

        print("\n================================")
        print("     BUS PASS MANAGEMENT SYSTEM")
        print("================================")
        print("1. Issue New Pass")
        print("2. Renew Existing Pass")
        print("3. Search Pass by ID")
        print("4. View All Passes")
        print("5. Exit")
        print("6. Edit Existing Pass")
        print("7. Delete Existing Pass")
        print("================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            issue_pass(passes)

        elif choice == "2":
            renew_pass(passes)

        elif choice == "3":
            search_pass(passes)

        elif choice == "4":
            view_passes(passes)

        elif choice == "5":
            print("Thank you for using our system!")
            break

        elif choice == "6":
            edit_pass(passes)

        elif choice == "7":
            delete_pass(passes)

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
